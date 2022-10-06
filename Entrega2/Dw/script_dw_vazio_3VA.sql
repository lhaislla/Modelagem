-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema dw_pedido
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema dw_pedido
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `dw_pedido` DEFAULT CHARACTER SET utf8mb3 ;
USE `dw_pedido` ;

-- -----------------------------------------------------
-- Table `dw_pedido`.`dimavaliacao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dw_pedido`.`dimavaliacao` (
  `key` INT NOT NULL AUTO_INCREMENT,
  `nota_avaliacao` VARCHAR(45) NULL DEFAULT NULL,
  `nota_avaliacao_descritivo` VARCHAR(45) NULL DEFAULT NULL,
  `date_from` TIMESTAMP NULL DEFAULT NULL,
  `date_to` TIMESTAMP NULL DEFAULT NULL,
  `version` INT NULL DEFAULT NULL,
  PRIMARY KEY (`key`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `dw_pedido`.`dimlocalizacao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dw_pedido`.`dimlocalizacao` (
  `key` INT NOT NULL AUTO_INCREMENT,
  `cidade` VARCHAR(45) NULL DEFAULT NULL,
  `estado_sigla` VARCHAR(45) NULL DEFAULT NULL,
  `date_from` TIMESTAMP NULL DEFAULT NULL,
  `date_to` TIMESTAMP NULL DEFAULT NULL,
  `version` INT NULL DEFAULT NULL,
  PRIMARY KEY (`key`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `dw_pedido`.`dimpagamento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dw_pedido`.`dimpagamento` (
  `key` INT NOT NULL AUTO_INCREMENT,
  `tipo_pagamento` VARCHAR(45) NULL DEFAULT NULL,
  `date_from` TIMESTAMP NULL DEFAULT NULL,
  `date_to` TIMESTAMP NULL DEFAULT NULL,
  `version` INT NULL DEFAULT NULL,
  PRIMARY KEY (`key`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `dw_pedido`.`dimproduto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dw_pedido`.`dimproduto` (
  `key` INT NOT NULL AUTO_INCREMENT,
  `categoria_produto` VARCHAR(45) NULL DEFAULT NULL,
  `date_from` TIMESTAMP NULL DEFAULT NULL,
  `date_to` TIMESTAMP NULL DEFAULT NULL,
  `version` INT NULL DEFAULT NULL,
  PRIMARY KEY (`key`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `dw_pedido`.`dimtempo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dw_pedido`.`dimtempo` (
  `key_data` INT NOT NULL AUTO_INCREMENT,
  `data_de_compra` DATETIME NULL DEFAULT NULL,
  `ano_numero` VARCHAR(45) NULL DEFAULT NULL,
  `mes_texto` VARCHAR(45) NULL DEFAULT NULL,
  `mes_numero` VARCHAR(45) NULL DEFAULT NULL,
  `mes_numero_ano` VARCHAR(45) NULL DEFAULT NULL,
  `dia_semana` VARCHAR(45) NULL DEFAULT NULL,
  `dia_semana_numero` VARCHAR(45) NULL DEFAULT NULL,
  `semana_numero_ano` VARCHAR(45) NULL DEFAULT NULL,
  `dia_numero_mes` VARCHAR(45) NULL DEFAULT NULL,
  `dia_numero_ano` VARCHAR(45) NULL DEFAULT NULL,
  `semana_nome` VARCHAR(45) NULL DEFAULT NULL,
  `dia_ehdiautil` INT NULL DEFAULT NULL,
  `semestre_texto` VARCHAR(45) NULL DEFAULT NULL,
  `semestre_numero` VARCHAR(45) NULL DEFAULT NULL,
  `semestre_numero_ano` VARCHAR(45) NULL DEFAULT NULL,
  `trimestre_texto` VARCHAR(45) NULL DEFAULT NULL,
  `trimestre_numero` INT NULL DEFAULT NULL,
  `trimestre_numero_ano` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`key_data`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `dw_pedido`.`fatopedido`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dw_pedido`.`fatopedido` (
  `valorPedido` DOUBLE NULL DEFAULT NULL,
  `dimAvaliacao_key` INT NULL DEFAULT NULL,
  `dimLocalizacao_key` INT NULL DEFAULT NULL,
  `dimPagamento_key` INT NULL DEFAULT NULL,
  `dimProduto_key` INT NULL DEFAULT NULL,
  `dimAtempo_key` INT NULL DEFAULT NULL,
  INDEX `dimAvaliacao_key_idx` (`dimAvaliacao_key` ASC) VISIBLE,
  INDEX `dimLocalizacao_key_idx` (`dimLocalizacao_key` ASC) VISIBLE,
  INDEX `dimPagamento_key_idx` (`dimPagamento_key` ASC) VISIBLE,
  INDEX `dimProduto_key_idx` (`dimProduto_key` ASC) VISIBLE,
  INDEX `dimTempo_key_idx` (`dimAtempo_key` ASC) VISIBLE,
  CONSTRAINT `dimAvaliacao_key`
    FOREIGN KEY (`dimAvaliacao_key`)
    REFERENCES `dw_pedido`.`dimavaliacao` (`key`),
  CONSTRAINT `dimLocalizacao_key`
    FOREIGN KEY (`dimLocalizacao_key`)
    REFERENCES `dw_pedido`.`dimlocalizacao` (`key`),
  CONSTRAINT `dimPagamento_key`
    FOREIGN KEY (`dimPagamento_key`)
    REFERENCES `dw_pedido`.`dimpagamento` (`key`),
  CONSTRAINT `dimProduto_key`
    FOREIGN KEY (`dimProduto_key`)
    REFERENCES `dw_pedido`.`dimproduto` (`key`),
  CONSTRAINT `dimTempo_key`
    FOREIGN KEY (`dimAtempo_key`)
    REFERENCES `dw_pedido`.`dimtempo` (`key_data`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
