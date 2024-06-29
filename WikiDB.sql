-- Active: 1710713821047@@localhost@3306@wikipediadb
DROP TABLE IF EXISTS `article_infos_final`;

CREATE TABLE `articles_info_final` (
    `ai_id_general` int unsigned NOT NULL DEFAULT 0,
    `ai_namespace` int NOT NULL DEFAULT 0,
    `ai_title` varbinary(255) NOT NULL DEFAULT '',
    `ai_id_revision` int NOT NULL DEFAULT 0,
    `ai_nb_links` int NOT NULL DEFAULT 0,
    PRIMARY KEY (`ai_id_general`,`ai_title`),
    KEY `ai_modif` (`ai_id_general`,`ai_id_revision`),
    KEY `ai_liens` (`ai_id_general`,`ai_nb_links`)
) ENGINE=InnoDB DEFAULT CHARSET=binary;

INSERT INTO `article_infos_final` VALUES (155,0,'Tval1',205610605,147),(145,0,'Tval2',7864524,15),(145,0,'Tval3',7864524,784),(125,0,'Tval4',278687,748)

SELECT * FROM article_infos_final;
SELECT DISTINCT `ai_namespace` FROM article_infos_final;
SELECT * FROM article_infos_final WHERE ai_namespace = 10; 
DELETE FROM article_infos_final

/* 0 4 6 8 10 12 14 100 102