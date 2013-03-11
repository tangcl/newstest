/*
Navicat MySQL Data Transfer

Source Server         : 202.85.136.60
Source Server Version : 50160
Source Host           : 202.85.136.60:3306
Source Database       : testnews

Target Server Type    : MYSQL
Target Server Version : 50160
File Encoding         : 65001

Date: 2013-03-10 15:16:01
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `ccategory`
-- ----------------------------
DROP TABLE IF EXISTS `ccategory`;
CREATE TABLE `ccategory` (
  `id` int(11) NOT NULL,
  `content` varchar(255) NOT NULL COMMENT '分类内容,由超级管理员admin创建,普通用户没有权限.',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ccategory
-- ----------------------------
INSERT INTO `ccategory` VALUES ('1', '军事');
INSERT INTO `ccategory` VALUES ('2', '游戏');

-- ----------------------------
-- Table structure for `info`
-- ----------------------------
DROP TABLE IF EXISTS `info`;
CREATE TABLE `info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `news_id` int(11) NOT NULL COMMENT '文章ID',
  `support_id` int(11) NOT NULL DEFAULT '0',
  `point_id` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of info
-- ----------------------------
INSERT INTO `info` VALUES ('1', '17', '3', '3');
INSERT INTO `info` VALUES ('2', '8', '1', '1');
INSERT INTO `info` VALUES ('3', '11', '1', '0');
INSERT INTO `info` VALUES ('4', '23', '2', '2');
INSERT INTO `info` VALUES ('5', '15', '1', '0');
INSERT INTO `info` VALUES ('6', '13', '1', '1');

-- ----------------------------
-- Table structure for `news`
-- ----------------------------
DROP TABLE IF EXISTS `news`;
CREATE TABLE `news` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `create_date` datetime NOT NULL,
  `status` tinyint(1) NOT NULL COMMENT '状态只有编辑中1,发布2,已删除0',
  `username` varchar(255) NOT NULL,
  `category` varchar(255) NOT NULL,
  `content` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of news
-- ----------------------------
INSERT INTO `news` VALUES ('7', 'dfsf', '2013-03-08 16:23:55', '1', 'admin', '军事', 'sadfsd');
INSERT INTO `news` VALUES ('6', 'fdsf', '2013-03-08 16:06:47', '1', 'admin', '军事', 'sfda');
INSERT INTO `news` VALUES ('8', '中国占领钓鱼岛', '2013-03-08 16:54:56', '1', 'admin', '军事', '中国占领钓鱼岛中国占领钓鱼岛中国占领钓鱼岛中国占领钓鱼岛中国占领钓鱼岛中国占领钓鱼岛中国占领钓鱼岛中国占领钓鱼岛中国占领钓鱼岛中国占领钓鱼岛中国占领钓鱼岛中国占领钓鱼岛');
INSERT INTO `news` VALUES ('9', '中国攻占日本东京', '2013-03-08 17:00:57', '2', 'admin', '军事', '中国攻占日本东京');
INSERT INTO `news` VALUES ('10', 'fdsad', '2013-03-08 17:01:10', '1', 'admin', '军事', 'asdfsaf');
INSERT INTO `news` VALUES ('11', '动态加载文章,异步请求', '2013-03-08 17:01:38', '1', 'admin', '军事', '很好的效果');
INSERT INTO `news` VALUES ('12', 'fdasfda', '2013-03-08 17:03:25', '1', 'admin', '军事', 'sdfadsfda');
INSERT INTO `news` VALUES ('13', 'fdasfda', '2013-03-08 17:03:38', '1', 'admin', '军事', 'sdfadsfdasaffda');
INSERT INTO `news` VALUES ('14', 'fdasfda', '2013-03-08 17:03:43', '2', 'admin', '军事', 'sdfadsfdasaffda');
INSERT INTO `news` VALUES ('15', 'DOTA是一个很好玩的游戏', '2013-03-08 19:00:34', '1', 'admin', '游戏', 'DOTA是一个很好玩的游戏DOTA是一个很好玩的游戏DOTA是一个很好玩的游戏DOTA是一个很好玩的游戏DOTA是一个很好玩的游戏');
INSERT INTO `news` VALUES ('16', '测试发布文章', '2013-03-08 19:01:33', '1', 'admin', '军事', 'fsafdafda');
INSERT INTO `news` VALUES ('17', '测试发布文章', '2013-03-08 19:07:26', '2', 'admin', '军事', '<strong>sdfafdas</strong>');
INSERT INTO `news` VALUES ('18', 'sdfas', '2013-03-08 19:29:02', '1', 'admin', '军事', 'asdfa');
INSERT INTO `news` VALUES ('19', 'sdfas', '2013-03-08 19:29:10', '1', 'admin', '军事', 'asdfafdsa');
INSERT INTO `news` VALUES ('20', 'sdfasfdad', '2013-03-08 19:30:31', '2', 'admin', '军事', 'asdfafdsasadfas');
INSERT INTO `news` VALUES ('21', 'daf', '2013-03-08 19:31:40', '2', 'admin', '军事', 'agdaga');
INSERT INTO `news` VALUES ('22', 'fdasfdsa', '2013-03-10 00:59:48', '2', 'admin', '军事', '<del>dfasdfadfa</del>');
INSERT INTO `news` VALUES ('23', 'fsafda', '2013-03-10 14:56:35', '2', 'tangcl', '军事', 'dasfdsaf');

-- ----------------------------
-- Table structure for `tuser`
-- ----------------------------
DROP TABLE IF EXISTS `tuser`;
CREATE TABLE `tuser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `createdate` datetime NOT NULL,
  `last_login` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_unique` (`name`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tuser
-- ----------------------------
INSERT INTO `tuser` VALUES ('1', 'admin', '21232f297a57a5a743894a0e4a801fc3', '2013-03-07 14:08:56', '2013-03-07 14:08:56');
INSERT INTO `tuser` VALUES ('3', 'tangcl', 'cc15ff521520a9cd0f161be9fad5774d', '2013-03-07 14:26:37', '2013-03-07 14:26:37');
INSERT INTO `tuser` VALUES ('4', 'cltang', '8e95207b2af38305fb6ac5634e33ecfb', '2013-03-10 14:58:54', '2013-03-10 14:58:54');
INSERT INTO `tuser` VALUES ('5', 'tangcl2', '359e3d1b90b277fd7d11126a66731154', '2013-03-10 14:59:17', '2013-03-10 14:59:17');
INSERT INTO `tuser` VALUES ('6', 'tangcl3', '71a1755b3ea43e0a62da18e3b690d98f', '2013-03-10 15:00:32', '2013-03-10 15:00:32');
INSERT INTO `tuser` VALUES ('7', 'tangcl4', '8726b89b423d0e99fba776c002353bf8', '2013-03-10 15:01:34', '2013-03-10 15:01:34');
