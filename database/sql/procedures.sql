-- AGENDAR UMA NOVA SESSAO
CREATE PROCEDURE agendar_sessao(
    IN p_mentor_id uuid,
    IN p_mentee_id uuid,
    IN p_scheduled_at timestamp,
    OUT nova_sessao_id uuid
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Verifica se mentor está disponível no horário
    IF NOT EXISTS (
        SELECT 1 FROM availability_slots
        WHERE mentor_id = p_mentor_id
          AND p_scheduled_at BETWEEN start_time AND end_time
    ) THEN
        RAISE EXCEPTION 'Mentor não disponível neste horário';
    END IF;

    -- Cria sessão
    INSERT INTO sessions (mentor_id, mentee_id, scheduled_at, status)
    VALUES (p_mentor_id, p_mentee_id, p_scheduled_at, 'scheduled')
    RETURNING id INTO nova_sessao_id;
END;
$$;

-- CRIAR PERFIL DE MENTORIA
CREATE OR REPLACE PROCEDURE criar_perfil_mentoria (
    IN p_bio TEXT,
    IN p_experience_level VARCHAR,
    IN p_user_id UUID,
    IN p_tech_stack_id INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Verifica se o par (user_id, tech_stack_id) existe na user_tech_stacks
    IF NOT EXISTS (
        SELECT 1 FROM user_tech_stacks
        WHERE users_id = p_user_id AND tech_stacks_id = p_tech_stack_id
    ) THEN
        RAISE EXCEPTION 'Par usuário/tech_stack não encontrado em user_tech_stacks';
    END IF;

    -- Cria perfil
    INSERT INTO mentorship_profiles (bio, experience_level, uts_user_id, uts_tech_stack_id)
    VALUES (p_bio, p_experience_level, p_user_id, p_tech_stack_id);
END;
$$;

-- INSERIR FEEDBACK
CREATE OR REPLACE PROCEDURE inserir_feedback (
    IN p_session_id UUID,
    IN p_rating INT,
    IN p_comment TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Verifica se a sessão existe
    IF NOT EXISTS (
        SELECT 1 FROM sessions WHERE id = p_session_id
    ) THEN
        RAISE EXCEPTION 'Sessão não encontrada';
    END IF;

    -- Insere feedback
    INSERT INTO feedbacks (session_id, rating, comment)
    VALUES (p_session_id, p_rating, p_comment);
END;
$$;

-- CANCELAR UMA SESSÃO
CREATE OR REPLACE PROCEDURE cancelar_sessao (
    IN p_session_id UUID
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Verifica se a sessão existe
    IF NOT EXISTS (
        SELECT 1 FROM sessions WHERE id = p_session_id
    ) THEN
        RAISE EXCEPTION 'Sessão não encontrada';
    END IF;

    -- Atualiza status
    UPDATE sessions
    SET status = 'cancelled'
    WHERE id = p_session_id;
END;
$$;
