CREATE DATABASE adm_simcc
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'pt_BR.UTF-8'
    LC_CTYPE = 'pt_BR.UTF-8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = FALSE;


CREATE EXTENSION IF NOT EXISTS "uuid-ossp";


DROP TABLE  IF EXISTS institution;
CREATE TABLE institution(
      institution_id SERIAL PRIMARY KEY,
      name VARCHAR(150) NOT NULL,
      acronym VARCHAR(20) NOT NULL,
      email_user VARCHAR(100) NOT NULL,
      PASSWORD  VARCHAR(100) NOT NULL,
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
      updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


DROP TABLE  IF EXISTS researcher;
CREATE TABLE researcher(
      researcher_id uuid NOT NULL DEFAULT uuid_generate_v4(),
      name VARCHAR(150) NOT NULL,
      lattes_id VARCHAR(20) NOT NULL,
      institution_id INTEGER NOT NULL,
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
      updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
      PRIMARY KEY (researcher_id),
      FOREIGN KEY (institution_id )
            REFERENCES institution (institution_id)
);


DROP TABLE  IF EXISTS graduate_program;
CREATE TABLE graduate_program(
      graduate_program_id uuid NOT NULL DEFAULT uuid_generate_v4(),
      code VARCHAR(100) NOT NULL,
      name VARCHAR(100) NOT NULL,
      area VARCHAR(100) NOT NULL,
      modality VARCHAR(100) NOT NULL,
      TYPE VARCHAR(100) NULL,
      rating VARCHAR(5),
      institution_id INTEGER NOT NULL,
      description VARCHAR(500) NULL,
      url_image VARCHAR(200) NULL,
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
      updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
      PRIMARY KEY (graduate_program_id),
      FOREIGN KEY (institution_id )
            REFERENCES institution (institution_id)

);

DROP TABLE  IF EXISTS graduate_program_researcher;
CREATE TABLE graduate_program_researcher(
      graduate_program_id uuid NOT NULL DEFAULT uuid_generate_v4(),
      researcher_id uuid NOT NULL DEFAULT uuid_generate_v4(),
      year INTEGER,
      type_ varchar(100),
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
      updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

      FOREIGN KEY (researcher_id )
            REFERENCES researcher (researcher_id),
      FOREIGN KEY (graduate_program_id )
            REFERENCES graduate_program (graduate_program_id)
);