CREATE DATABASE IF NOT EXISTS master_python;
USE master_python;

CREATE TABLE usuarios(
id int auto_increment,
nombre varchar(100),
apellidos varchar(255),
email varchar(255) not null,
password varchar(255) not null,
fecha date not null,
CONSTRAINT pk_usuarios PRIMARY KEY(id),
CONSTRAINT uq_email UNIQUE(email)
)ENGINE=innodb;

CREATE TABLE notas(
id int auto_increment,
usuario_id int not null,
titulo varchar(255) not null,
descripcion mediumtext,
fecha date not null,
CONSTRAINT pk_notas PRIMARY KEY(id),
CONSTRAINT fk_nota_usuario
    FOREIGN KEY(usuario_id)
    REFERENCES usuarios(id)
    ON DELETE NO ACTION NO UPDATE NO ACTION
)ENGINE=innodb;