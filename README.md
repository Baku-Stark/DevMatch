# 🔥 Desafio Full Stack: `DevMatch – Plataforma de Mentoria entre Desenvolvedores`

Sobre o projeto: O DevMatch é uma plataforma de mentoria entre devs, conectando mentores e mentorados com base em tecnologias dominadas, experiência e disponibilidade.

### 🎯 Objetivo

Criar uma plataforma onde desenvolvedores possam **se cadastrar como mentores ou mentorados**, marcar sessões, compartilhar conhecimento, e construir reputação na comunidade.

---

### 🧩 Funcionalidades Principais

#### 👤 | Autenticação e Autorização

* Login com OAuth2 (GitHub ou Google) + JWT
* Perfis públicos com dados técnicos, bio, links, etc.
* Dois tipos de usuários: `Mentor` e `Mentorado` (ou ambos)

#### 🔍 | Sistema de Match

* Algoritmo de matching baseado em:

  * Stack (ex: React + Node)
  * Nível de experiência
  * Idioma preferido
  * Disponibilidade

#### 📆 | Agendamento de Sessões

* Sistema de calendários sincronizados com disponibilidade
* Marcação e confirmação de sessões
* Integração com Google Calendar (opcional)

#### 📊 | Dashboard

* Para mentores: sessões marcadas, feedbacks recebidos, notas
* Para mentorados: progresso, histórico, sugestões de novos matches

#### 📝 | Feedback e Avaliações

* Após cada sessão, o mentorado deixa um feedback (1 a 5 estrelas + comentário)
* Reputação pública dos mentores cresce com base em avaliações

#### 💬 | Chat em Tempo Real

* WebSockets (com socket.io ou alternativa)
* Sala privada entre mentor e mentorado após agendamento

---

### 🏗️ | Stack Sugerida

#### Backend:

* **Node.js com TypeScript** ou **Python (FastAPI)**
* **PostgreSQL** (relacional ideal para esse tipo de lógica)
* **Prisma** ou **SQLAlchemy**
* Autenticação com JWT + OAuth2

#### Frontend:

* **React** + **TypeScript**
* **Tailwind CSS** + **Headless UI**
* State management com **Zustand** ou **Redux Toolkit**
* API consumption via **React Query**

#### Extras (Desafio Avançado):

* CI/CD com GitHub Actions + Docker
* Testes: Jest no front, Pytest ou Vitest no back
* Deploy no Render/Vercel/Netlify (front) e Railway/Render (back)
* Containerização com Docker Compose
* Integração com Stripe (caso queira monetização opcional para sessões)

---

# Banco de Dados

### **Relatório Técnico – Banco de Dados DevMatch**

<details>

<summary><b>📄 | Clique aqui para obter mais informações</b></summary>

### Data: 26/06/2025

### Desenvolvedor: Baku-Stark

---

## **Modelagem de Dados**

O banco foi modelado com base em entidades reais do domínio do sistema, utilizando boas práticas de **normalização**, **relacionamentos fortes** e **flexibilidade para escalabilidade futura**.

---

## **Tabelas Criadas**

| Tabela                | Descrição                                                             |
| --------------------- | --------------------------------------------------------------------- |
| `users`               | Usuários da plataforma (mentores e mentorados)                        |
| `tech_stacks`         | Tecnologias (React, Node, etc.)                                       |
| `languages`           | Idiomas (Português, Inglês, etc.)                                     |
| `user_tech_stacks`    | Relaciona usuários às stacks (N:N)                                   |
| `user_languages`      | Relaciona usuários aos idiomas (N:N)                                 |
| `mentorship_profiles` | Perfil de mentoria, associando usuário e stack, com bio e experiência |
| `availability_slots`  | Horários disponíveis dos mentores                                     |
| `sessions`            | Sessões de mentoria agendadas entre mentor e mentorado                |
| `feedbacks`           | Avaliações e comentários pós-sessão                                   |

---

## **Relacionamentos Chave**

* `users` ⇄ `tech_stacks` → via `user_tech_stacks`
* `users` ⇄ `languages` → via `user_languages`
* `users` ⇄ `sessions` → (mentor\_id e mentee\_id)
* `users` ⇄ `availability_slots` → apenas mentores
* `mentorship_profiles` ⇄ `user_tech_stacks`
* `sessions` ⇄ `feedbacks`

---

## **Normalização & Tabelas de Apoio**

Foram aplicadas **3FN**:

* Stack e idiomas foram extraídos para tabelas próprias (`tech_stacks`, `languages`)
* Tabelas de junção (`user_tech_stacks`, `user_languages`) garantem relacionamentos n\:N

---

## **Stored Procedures Implementadas**

| Nome                    | Finalidade                                         |
| ----------------------- | -------------------------------------------------- |
| `agendar_sessao`        | Verifica disponibilidade do mentor e agenda sessão |
| `cancelar_sessao`       | Altera status da sessão para cancelada             |
| `inserir_feedback`      | Registra avaliação de uma sessão concluída         |
| `criar_perfil_mentoria` | Associa tech stack ao mentor e cria perfil         |
| `registrar_usuario`     | Cria novo usuário e associa stacks e idiomas       |

---

## **VIEWS, INDEXES e TRIGGERS**

Foram **especificados**, mas não detalhados neste escopo final, por decisão do PO de encerrar a parte do banco.

Possíveis sugestões para depois:

* **Views** para dashboards (sessões por mentor, média de rating)
* **Triggers** para logs de sessões
* **Indexes** em campos como `email`, `created_at`, `tech_stacks_id`, `languages_id`

---

## **Tecnologias Usadas**

* **SGBD**: PostgreSQL
* **PKs**: UUIDs para entidades principais
* **Chaves Estrangeiras**: com `ON DELETE CASCADE`
* **Funções**: escritas em **PL/pgSQL**

---

## **Status Final**

| Item                      | Status                         |
| ------------------------- | ------------------------------ |
| **Modelagem ER**              | ✅                              |
| **Criação do Schema**         | ✅                              |
| **Normalização até 3FN**      | ✅                              |
| **Foreign Keys**              | ✅                              |
| **Stored Procedures**         | ✅                              |
| **Inserções Exemplo**         | ✅                              |
| **Views/Triggers** | ✅ |
| **Documentação Técnica**      | ✅                              |

</details>

### **Relatório Técnico – Backend DevMatch**

<details>

<summary><b>📄 | Clique aqui para obter mais informações</b></summary>

>[!NOTE]
> Para informações mais detalhadas da API: [Clique Aqui](/api/README.md)

</details>