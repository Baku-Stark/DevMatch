-- [VIEWS] – Consultas reutilizáveis e simplificadas
-- view_mentor_profiles : Mostra todos os perfis de mentoria com nome do mentor, tech stack, nível de experiência e bio.
CREATE OR REPLACE VIEW view_mentor_profiles AS
SELECT 
    u.id AS user_id,
    u.name AS mentor_name,
    ts.name AS tech_stack,
    mp.experience_level,
    mp.bio
FROM mentorship_profiles mp
JOIN user_tech_stacks uts ON mp.uts_user_id = uts.users_id AND mp.uts_tech_stack_id = uts.tech_stacks_id
JOIN users u ON u.id = uts.users_id
JOIN tech_stacks ts ON ts.id = uts.tech_stacks_id
WHERE u.role = 'mentor';

-- view_scheduled_sessions : Mostra todas as sessões futuras agendadas com nomes dos participantes.
CREATE OR REPLACE VIEW view_scheduled_sessions AS
SELECT 
    s.id AS session_id,
    s.scheduled_at,
    s.status,
    mentor.name AS mentor_name,
    mentee.name AS mentee_name
FROM sessions s
JOIN users mentor ON mentor.id = s.mentor_id
JOIN users mentee ON mentee.id = s.mentee_id
WHERE s.status = 'scheduled';

-- [INDEXES] – Melhorando velocidade de busca
-- Usuários
CREATE INDEX idx_users_email ON users (email);

-- Sessions
CREATE INDEX idx_sessions_scheduled_at ON sessions (scheduled_at);
CREATE INDEX idx_sessions_status ON sessions (status);

-- Feedbacks
CREATE INDEX idx_feedbacks_session_id ON feedbacks (session_id);

-- user_tech_stacks
CREATE INDEX idx_user_tech_stacks_user_id ON user_tech_stacks (users_id);
CREATE INDEX idx_user_tech_stacks_stack_id ON user_tech_stacks (tech_stacks_id);

-- user_languages
CREATE INDEX idx_user_languages_user_id ON user_languages (users_id);
CREATE INDEX idx_user_languages_lang_id ON user_languages (languages_id);

-- mentorship_profiles
CREATE INDEX idx_mentorship_profiles_user_stack ON mentorship_profiles (uts_user_id, uts_tech_stack_id);

-- [TRIGGER] para limpar sessões canceladas antigas
-- updated_at para usuários
-- Adicionar coluna opcional
ALTER TABLE users ADD COLUMN updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP;

-- Criar função
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Criar trigger
CREATE TRIGGER trg_update_users_updated_at
BEFORE UPDATE ON users
FOR EACH ROW
EXECUTE FUNCTION update_timestamp();

-- Criar função
CREATE OR REPLACE FUNCTION delete_old_cancelled_sessions()
RETURNS TRIGGER AS $$
BEGIN
    DELETE FROM sessions WHERE status = 'cancelled' AND scheduled_at < NOW() - INTERVAL '30 days';
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

-- Trigger após inserir/cancelar sessão
CREATE TRIGGER trg_cleanup_cancelled_sessions
AFTER INSERT OR UPDATE ON sessions
FOR EACH STATEMENT
EXECUTE FUNCTION delete_old_cancelled_sessions();
