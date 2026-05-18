create database db_importdados;

use db_importdados;

CREATE TABLE TB_TITULOS(
    IDTitulo INT primary KEY auto_increment,
    Descricao varchar(120),
    DataTitulo date,
    DataVencimento date,
    IDCliente INT,
    NaturezaTitulo varchar(50),
    ValorTitulo float,
    SituacaoTitulo char(20)
);


create table log_Titulo (
	idlog int primary key auto_increment,
	idtitulo int,
	datalog date,
	valor_old float,
	valor_new float,
	situacao char(25)
);

create or replace view VW_Resumo_Titulos as select situacaotitulo,
    count(*) as Qtde_titulos,
    sum(ValorTitulo) as Total_Valor,
    count(case when SituacaoTitulo='PENDENTE' then 1 else 0 end) as Pendente,
    count(case when SituacaoTitulo='QUITADO' then 1 else 0 end) as Quitado from TB_TITULOS group by situacaotitulo
;

DELIMITER $$

CREATE TRIGGER TR_Baixar_Titulo
AFTER UPDATE ON TB_TITULOS
FOR EACH ROW
BEGIN
    INSERT INTO LOG_TITULO (
        IDTitulo,
        DataLog,
        Valor_Old,
        Valor_New,
        Situacao
    )
    VALUES (
        NEW.IDTitulo,
        CURDATE(),
        OLD.ValorTitulo,
        NEW.ValorTitulo,
        NEW.SituacaoTitulo
    );
END$$

DELIMITER ;
