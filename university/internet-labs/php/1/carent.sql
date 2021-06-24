-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 31, 2018 at 01:02 PM
-- Server version: 5.7.11-0ubuntu6
-- PHP Version: 7.0.4-7ubuntu2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `carent`
--

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `customer_id` int(10) UNSIGNED NOT NULL,
  `name` varchar(30) NOT NULL DEFAULT '',
  `address` varchar(80) NOT NULL DEFAULT '',
  `phone` varchar(15) NOT NULL DEFAULT '',
  `discount` double NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`customer_id`, `name`, `address`, `phone`, `discount`) VALUES
(1001, 'John Teck', '8 Happy Ave', '88888888', 0.1),
(1002, 'Mohammed Ali', '10 Chester Road', '99999999', 0.15),
(1003, 'Kumar', '5 Serangoon Road', '55555555', 0),
(1004, 'Kevin Jones', '2 Sunset boulevard', '22222222', 0.2);

-- --------------------------------------------------------

--
-- Table structure for table `rent_records`
--

CREATE TABLE `rent_records` (
  `rent_id` int(10) UNSIGNED NOT NULL,
  `reg_no` varchar(8) NOT NULL,
  `customer_id` int(10) UNSIGNED NOT NULL,
  `start_date` date NOT NULL DEFAULT '2018-01-01',
  `end_date` date NOT NULL DEFAULT '2018-12-12',
  `lastUpdated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `rent_records`
--

INSERT INTO `rent_records` (`rent_id`, `reg_no`, `customer_id`, `start_date`, `end_date`, `lastUpdated`) VALUES
(1, 'BA6611A', 1001, '2018-01-01', '2018-01-21', '2018-05-31 12:02:13'),
(2, 'BA6611A', 1001, '2018-02-01', '2018-02-05', '2018-05-31 12:02:13'),
(3, 'GA5955E', 1003, '2018-01-05', '2018-01-31', '2018-05-31 12:02:13'),
(4, 'GA6666F', 1004, '2018-01-20', '2018-02-20', '2018-05-31 12:02:13');

-- --------------------------------------------------------

--
-- Table structure for table `vehicles`
--

CREATE TABLE `vehicles` (
  `reg_no` varchar(8) NOT NULL,
  `category` enum('car','truck') NOT NULL DEFAULT 'car',
  `brand` varchar(30) DEFAULT '"',
  `description` varchar(256) DEFAULT '"',
  `photo` blob,
  `daily_rate` decimal(6,2) NOT NULL DEFAULT '9.99'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `vehicles`
--

INSERT INTO `vehicles` (`reg_no`, `category`, `brand`, `description`, `photo`, `daily_rate`) VALUES
('BA6611A', 'car', 'NISSAN SUNNY 1.6L', '4 Door Saloon, Automatic', NULL, '9.99'),
('GA5955E', 'truck', 'NISSAN CABSTAR 3.0L', 'Lorry, Manual ', NULL, '8.99'),
('GA6666F', 'truck', 'OPEL COMBO 1.6L', 'Van, Manual', NULL, '6.99'),
('SB6522B', 'car', 'TOYOTA ALTIS 1.6L', '4 Door Saloon, Automatic', NULL, '9.99'),
('SB6733C', 'car', 'HONDA CIVIC 1.8L', '4 Door Saloon, Automatic', NULL, '11.99');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`customer_id`),
  ADD UNIQUE KEY `phone` (`phone`),
  ADD KEY `name` (`name`);

--
-- Indexes for table `rent_records`
--
ALTER TABLE `rent_records`
  ADD PRIMARY KEY (`rent_id`),
  ADD KEY `customer_id` (`customer_id`),
  ADD KEY `reg_no` (`reg_no`);

--
-- Indexes for table `vehicles`
--
ALTER TABLE `vehicles`
  ADD PRIMARY KEY (`reg_no`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customers`
--
ALTER TABLE `customers`
  MODIFY `customer_id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1006;
--
-- AUTO_INCREMENT for table `rent_records`
--
ALTER TABLE `rent_records`
  MODIFY `rent_id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `rent_records`
--
ALTER TABLE `rent_records`
  ADD CONSTRAINT `rent_records_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`customer_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `rent_records_ibfk_2` FOREIGN KEY (`reg_no`) REFERENCES `vehicles` (`reg_no`) ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
