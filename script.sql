CREATE DATABASE adm_simcc
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Portuguese_Brazil.1252'
    LC_CTYPE = 'Portuguese_Brazil.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = FALSE;

DROP TABLE  IF EXISTS institution;
CREATE TABLE adm_institution(
      institution_id SERIAL PRIMARY KEY,
      name VARCHAR(150) NOT NULL,
      acronym VARCHAR(20) NOT NULL,
      email_user VARCHAR(100) NOT NULL,
      PASSWORD  VARCHAR(100) NOT NULL
);


DROP TABLE  IF EXISTS researcher;
CREATE TABLE adm_researcher(
      researcher_id SERIAL PRIMARY KEY,
      name VARCHAR(150) NOT NULL,
      lattes_id VARCHAR(20) NOT NULL,
      institution_id INTEGER NOT NULL,
      FOREIGN KEY (institution_id )
            REFERENCES adm_institution (institution_id)
);


DROP TABLE  IF EXISTS graduate_program;
CREATE TABLE adm_graduate_program(
      graduate_program_id SERIAL PRIMARY KEY,
      code VARCHAR(100) NOT NULL,
      name VARCHAR(100) NOT NULL,
      area VARCHAR(100) NOT NULL,
      modality VARCHAR(100) NOT NULL,
      TYPE VARCHAR(100) NULL,
      rating VARCHAR(5),
      institution_id INTEGER NOT NULL,
      FOREIGN KEY (institution_id )
            REFERENCES adm_graduate_program (institution_id)

);

DROP TABLE  IF EXISTS graduate_program_researcher;
      CREATE TABLE adm_graduate_program_researcher(
      graduate_program_id  integer ,
      researcher_id INTEGER,
      year INTEGER,
      type_ varchar(100),

      PRIMARY KEY (graduate_program_id,researcher_id,year),
      FOREIGN KEY (researcher_id )
            REFERENCES researcher (researcher_id),
      FOREIGN KEY (graduate_program_id )
            REFERENCES adm_graduate_program_researcher (graduate_program_id)
);