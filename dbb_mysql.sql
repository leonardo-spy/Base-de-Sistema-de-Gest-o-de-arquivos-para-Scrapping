/*
MySQL Backup
Database: CENSURADO
Backup Time: 2022-01-17 16:47:15
*/

SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS `cliente_docs_em_processo`;
DROP TABLE IF EXISTS `cliente_licenca`;
DROP TABLE IF EXISTS `cliente_maquina`;
DROP TABLE IF EXISTS `clientes_arquivos`;
DROP TABLE IF EXISTS `clientes_senha`;
DROP TABLE IF EXISTS `resultado_servico0`;
DROP TABLE IF EXISTS `resultado_servico1`;
DROP TABLE IF EXISTS `resultado_servico2`;
CREATE TABLE `cliente_docs_em_processo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `documento` bigint(20) NOT NULL,
  `processado` tinyint(4) DEFAULT 0,
  `atuando` datetime DEFAULT NULL ON UPDATE current_timestamp(),
  `arquivo` int(11) NOT NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `id` (`id`,`documento`,`processado`,`atuando`,`arquivo`) USING BTREE,
  KEY `arquivo` (`arquivo`,`processado`) USING BTREE,
  KEY `arquivo2` (`arquivo`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;
CREATE TABLE `cliente_licenca` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ativo` tinyint(1) NOT NULL DEFAULT 0,
  `nome_cliente` varchar(60) NOT NULL,
  `data_expiracao` datetime NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;
CREATE TABLE `cliente_maquina` (
  `uuid` bigint(20) NOT NULL,
  `idcliente` int(11) NOT NULL DEFAULT 0,
  KEY `id` (`idcliente`,`uuid`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
CREATE TABLE `clientes_arquivos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cliente` int(11) NOT NULL DEFAULT 0,
  `ativo` int(11) NOT NULL DEFAULT 0,
  `nome` varchar(255) DEFAULT NULL,
  `servico` int(11) NOT NULL DEFAULT 1,
  `atuando` datetime DEFAULT NULL ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`) USING BTREE,
  KEY `id` (`id`,`cliente`,`ativo`) USING BTREE,
  KEY `cliente` (`cliente`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;
CREATE TABLE `clientes_senha` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cliente` int(11) NOT NULL DEFAULT 0,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `secreta` tinyint(1) NOT NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `id` (`id`,`cliente`,`username`,`password`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
CREATE TABLE `resultado_servico0` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `documento` bigint(20) NOT NULL,
  `resultado` varchar(20) DEFAULT '0',
  `arquivo` int(11) NOT NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `id` (`id`,`documento`,`resultado`,`arquivo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
CREATE TABLE `resultado_servico1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `documento` bigint(20) NOT NULL,
  `resultado` varchar(20) DEFAULT '0',
  `arquivo` int(11) NOT NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `id` (`id`,`documento`,`resultado`,`arquivo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
CREATE TABLE `resultado_servico2` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `documento` bigint(20) NOT NULL,
  `resultado` varchar(20) DEFAULT '0',
  `arquivo` int(11) NOT NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `id` (`id`,`documento`,`resultado`,`arquivo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

