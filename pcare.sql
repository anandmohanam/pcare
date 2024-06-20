-- phpMyAdmin SQL Dump
-- version 3.3.9
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 25, 2021 at 04:53 AM
-- Server version: 5.5.8
-- PHP Version: 5.3.5

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `pcare`
--

-- --------------------------------------------------------

--
-- Table structure for table `authorityreg`
--

CREATE TABLE IF NOT EXISTS `authorityreg` (
  `aregister_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `aid` varchar(100) NOT NULL,
  `office` varchar(100) NOT NULL,
  `phno` varchar(100) NOT NULL,
  `district` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `role` varchar(100) NOT NULL,
  PRIMARY KEY (`aregister_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `authorityreg`
--

INSERT INTO `authorityreg` (`aregister_id`, `name`, `aid`, `office`, `phno`, `district`, `email`, `password`, `role`) VALUES
(2, 'mahesh', '20145', 'pension seva', '1234567891', 'None', 'al@gmail.com', '33333', 'Authority'),
(3, 'DILSHA DELEEP', '895', 'pension seva', '9567892977', 'None', 'DIL@GMAIL.COM', '123456789', 'Authority');

-- --------------------------------------------------------

--
-- Table structure for table `clerkreg`
--

CREATE TABLE IF NOT EXISTS `clerkreg` (
  `clerk_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `aid` varchar(100) NOT NULL,
  `office` varchar(100) NOT NULL,
  `phno` varchar(100) NOT NULL,
  `district` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `role` varchar(100) NOT NULL,
  PRIMARY KEY (`clerk_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `clerkreg`
--


-- --------------------------------------------------------

--
-- Table structure for table `deposit`
--

CREATE TABLE IF NOT EXISTS `deposit` (
  `deposit_id` int(11) NOT NULL AUTO_INCREMENT,
  `aregister_id` varchar(100) NOT NULL COMMENT 'foreign key',
  `bank_name` varchar(100) NOT NULL,
  `month` varchar(100) NOT NULL,
  `amount` varchar(100) NOT NULL,
  PRIMARY KEY (`deposit_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=23 ;

--
-- Dumping data for table `deposit`
--

INSERT INTO `deposit` (`deposit_id`, `aregister_id`, `bank_name`, `month`, `amount`) VALUES
(19, '9567892977', '8089186044', 'January', '1000'),
(20, '9567892977', '8089186044', 'February', '1000'),
(21, '9567892977', '8089186044', 'March', '1000'),
(22, '9567892977', '9496717549', 'January', '1000');

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE IF NOT EXISTS `feedback` (
  `feed_id` int(100) NOT NULL AUTO_INCREMENT,
  `user_id` varchar(100) NOT NULL,
  `message` varchar(200) NOT NULL,
  PRIMARY KEY (`feed_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `feedback`
--

INSERT INTO `feedback` (`feed_id`, `user_id`, `message`) VALUES
(1, '8089186044', 'very nice app'),
(2, '8089186044', 'regvgh'),
(3, '9567892977', 'nice app'),
(4, '9567892977', 'nice app');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE IF NOT EXISTS `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `register_id` varchar(100) NOT NULL COMMENT 'foreign key',
  `user_name` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `role` varchar(100) NOT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=12 ;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`login_id`, `register_id`, `user_name`, `password`, `role`) VALUES
(1, '1', '7012698790', '33333', 'admin'),
(8, '9', '8089186044', '12345', 'public'),
(9, '2', '1234567891', '33333', 'authority'),
(10, '3', '9567892977', '123456789', 'authority'),
(11, '10', '9496717549', '12345', 'public');

-- --------------------------------------------------------

--
-- Table structure for table `pension`
--

CREATE TABLE IF NOT EXISTS `pension` (
  `pension_id` int(11) NOT NULL AUTO_INCREMENT,
  `register_id` varchar(100) NOT NULL COMMENT 'foreign key',
  `category` varchar(100) NOT NULL,
  `bank` varchar(50) NOT NULL,
  `proof` varchar(50) NOT NULL,
  `status` varchar(100) NOT NULL,
  `amount` varchar(25) NOT NULL,
  PRIMARY KEY (`pension_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=16 ;

--
-- Dumping data for table `pension`
--

INSERT INTO `pension` (`pension_id`, `register_id`, `category`, `bank`, `proof`, `status`, `amount`) VALUES
(14, '8089186044', 'Adult pension Yojana', '1234567890', 'virat-2_DCCdDk7.jpg', 'approved', '1000'),
(15, '9496717549', 'Adult pension Yojana', '12345678912', 'virat-2_VlAJ08j.jpg', 'approved', '1000');

-- --------------------------------------------------------

--
-- Table structure for table `pensionplans`
--

CREATE TABLE IF NOT EXISTS `pensionplans` (
  `plan_id` int(11) NOT NULL AUTO_INCREMENT,
  `planname` varchar(50) NOT NULL,
  `description` varchar(500) NOT NULL,
  `amount` varchar(25) NOT NULL,
  PRIMARY KEY (`plan_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=9 ;

--
-- Dumping data for table `pensionplans`
--

INSERT INTO `pensionplans` (`plan_id`, `planname`, `description`, `amount`) VALUES
(2, 'Adult pension Yojana', 'Atal Pension Yojana (APY), a pension scheme for workers in the unorganised sector like personal maids, drivers, gardeners etc, was launched in June 2015 by the government. ... APY aims to help these workers save money for their old age while they are working and guarantees returns post retirement.', '1000'),
(8, 'widow pension yojana', 'to provide financial support to the poor widows in india , the widow pension yojana was introduced .per month 1000 rs', '1000');

-- --------------------------------------------------------

--
-- Table structure for table `userreg`
--

CREATE TABLE IF NOT EXISTS `userreg` (
  `register_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `age` varchar(100) NOT NULL,
  `phno` varchar(100) NOT NULL,
  `dob` date NOT NULL,
  `gender` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `role` varchar(100) NOT NULL,
  PRIMARY KEY (`register_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=11 ;

--
-- Dumping data for table `userreg`
--

INSERT INTO `userreg` (`register_id`, `name`, `address`, `age`, `phno`, `dob`, `gender`, `email`, `password`, `role`) VALUES
(8, 'yedhu', 'chirayath', '49', '9496169877', '1991-07-18', 'male', '789@gmail.com', '33333', 'public'),
(9, 'anu', 'maliyekkal', '49', '8089186044', '1986-10-15', 'female', 'anu@gmail.com', '12345', 'public'),
(10, 'anjitha', 'jkhgfj[og', '35', '9496717549', '1988-01-07', 'female', 'anjitha@gmail.com', '12345', 'public');
