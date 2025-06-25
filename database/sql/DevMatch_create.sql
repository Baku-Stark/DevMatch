-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2025-06-25 09:14:15.858

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- tables
-- Table: availability_slots
CREATE TABLE availability_slots (
    id int  NOT NULL,
    mentor_id uuid  NOT NULL,
    start_time timestamp  NOT NULL DEFAULT CURRENT_TIMESTAMP,
    end_time timestamp  NOT NULL DEFAULT CURRENT_TIMESTAMP,
    timezone varchar(50)  NOT NULL,
    CONSTRAINT availability_slots_pk PRIMARY KEY (id)
);

-- Table: feedbacks
CREATE TABLE feedbacks (
    id uuid  NOT NULL,
    session_id uuid  NOT NULL,
    rating int  NOT NULL,
    comment text  NOT NULL,
    created_at timestamp  NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT feedbacks_pk PRIMARY KEY (id)
);

-- Table: languages
CREATE TABLE languages (
    id serial  NOT NULL,
    language varchar(50)  NOT NULL,
    CONSTRAINT languages_unq UNIQUE (language) NOT DEFERRABLE  INITIALLY IMMEDIATE,
    CONSTRAINT languages_pk PRIMARY KEY (id)
);

-- Table: mentorship_profiles
CREATE TABLE mentorship_profiles (
    id uuid  NOT NULL,
    bio text  NOT NULL,
    experience_level varchar(25)  NOT NULL,
    uts_user_id uuid  NOT NULL,
    uts_tech_stack_id int  NOT NULL,
    CONSTRAINT mentorship_profiles_pk PRIMARY KEY (id)
);

-- Table: sessions
CREATE TABLE sessions (
    id uuid  NOT NULL,
    mentor_id uuid  NOT NULL,
    mentee_id uuid  NOT NULL,
    scheduled_at timestamp  NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status varchar(25)  NOT NULL,
    created_at timestamp  NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT sessions_pk PRIMARY KEY (id)
);

-- Table: tech_stacks
CREATE TABLE tech_stacks (
    id serial  NOT NULL,
    name varchar(25)  NOT NULL,
    CONSTRAINT tech_stacks_pk PRIMARY KEY (id)
);

-- Table: user_languages
CREATE TABLE user_languages (
    users_id uuid  NOT NULL,
    languages_id int  NOT NULL,
    CONSTRAINT user_languages_pk PRIMARY KEY (users_id,languages_id)
);

-- Table: user_tech_stacks
CREATE TABLE user_tech_stacks (
    users_id uuid  NOT NULL,
    tech_stacks_id serial  NOT NULL,
    CONSTRAINT user_tech_stacks_pk PRIMARY KEY (users_id,tech_stacks_id)
);

-- Table: users
CREATE TABLE users (
    id uuid  NOT NULL DEFAULT uuid_generate_v4(),
    name varchar(255)  NOT NULL,
    email varchar(255)  NOT NULL,
    role varchar(20)  NOT NULL,
    avatar_url text  NOT NULL,
    created_at timestamp  NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT uniq_email UNIQUE (email) NOT DEFERRABLE  INITIALLY IMMEDIATE,
    CONSTRAINT users_pk PRIMARY KEY (id)
);

-- foreign keys
-- Reference: availability_slots_users_mentor (table: availability_slots)
ALTER TABLE availability_slots ADD CONSTRAINT availability_slots_users_mentor
    FOREIGN KEY (mentor_id)
    REFERENCES users (id)
    ON DELETE  CASCADE 
    ON UPDATE  CASCADE 
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: feedbacks_sessions (table: feedbacks)
ALTER TABLE feedbacks ADD CONSTRAINT feedbacks_sessions
    FOREIGN KEY (session_id)
    REFERENCES sessions (id)
    ON DELETE  CASCADE 
    ON UPDATE  CASCADE 
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: mentorship_profiles_user_tech_stacks (table: mentorship_profiles)
ALTER TABLE mentorship_profiles ADD CONSTRAINT mentorship_profiles_user_tech_stacks
    FOREIGN KEY (uts_user_id, uts_tech_stack_id)
    REFERENCES user_tech_stacks (users_id, tech_stacks_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: sessions_mentee (table: sessions)
ALTER TABLE sessions ADD CONSTRAINT sessions_mentee
    FOREIGN KEY (mentee_id)
    REFERENCES users (id)
    ON DELETE  CASCADE 
    ON UPDATE  CASCADE 
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: sessions_mentor (table: sessions)
ALTER TABLE sessions ADD CONSTRAINT sessions_mentor
    FOREIGN KEY (mentor_id)
    REFERENCES users (id)
    ON DELETE  CASCADE 
    ON UPDATE  CASCADE 
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: user_languages_languages (table: user_languages)
ALTER TABLE user_languages ADD CONSTRAINT user_languages_languages
    FOREIGN KEY (languages_id)
    REFERENCES languages (id)
    ON DELETE  CASCADE 
    ON UPDATE  CASCADE 
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: user_languages_users (table: user_languages)
ALTER TABLE user_languages ADD CONSTRAINT user_languages_users
    FOREIGN KEY (users_id)
    REFERENCES users (id)
    ON DELETE  CASCADE 
    ON UPDATE  CASCADE 
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: user_tech_stacks_tech_stacks (table: user_tech_stacks)
ALTER TABLE user_tech_stacks ADD CONSTRAINT user_tech_stacks_tech_stacks
    FOREIGN KEY (tech_stacks_id)
    REFERENCES tech_stacks (id)
    ON DELETE  CASCADE 
    ON UPDATE  CASCADE 
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: user_tech_stacks_users (table: user_tech_stacks)
ALTER TABLE user_tech_stacks ADD CONSTRAINT user_tech_stacks_users
    FOREIGN KEY (users_id)
    REFERENCES users (id)
    ON DELETE  CASCADE 
    ON UPDATE  CASCADE 
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.

