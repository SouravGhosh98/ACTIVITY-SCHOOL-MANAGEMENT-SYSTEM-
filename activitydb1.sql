-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 03, 2022 at 06:31 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `activitydb1`
--

-- --------------------------------------------------------

--
-- Table structure for table `admission`
--

CREATE TABLE `admission` (
  `batchid` int(11) DEFAULT NULL,
  `emailid` varchar(40) DEFAULT NULL,
  `admissionno` int(11) NOT NULL,
  `admissiondate` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admission`
--

INSERT INTO `admission` (`batchid`, `emailid`, `admissionno`, `admissiondate`) VALUES
(1, 'kavita@gmail.com', 1, '2022-05-12'),
(2, 'nidhi@gmail.com', 2, '2022-05-12'),
(1, 'nidhi@gmail.com', 3, '2022-05-12'),
(1, 'deepak@gmail.com', 4, '2022-07-16'),
(1, 'monusenb93@gmail.com', 5, '2022-09-01'),
(4, 'monusenb93@gmail.com', 6, '2022-09-01');

-- --------------------------------------------------------

--
-- Table structure for table `batch1`
--

CREATE TABLE `batch1` (
  `courseid` int(11) DEFAULT NULL,
  `batchid` int(11) NOT NULL,
  `startdate` date DEFAULT NULL,
  `batchtime` varchar(20) DEFAULT NULL,
  `facultynm` varchar(40) DEFAULT NULL,
  `batchstatus` tinyint(4) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `batch1`
--

INSERT INTO `batch1` (`courseid`, `batchid`, `startdate`, `batchtime`, `facultynm`, `batchstatus`) VALUES
(1, 1, '2022-05-17', '6 to 7 pm', 'ritu jain', 1),
(2, 2, '2022-05-20', '4 to 5 pm', 'ritu jain', 1),
(2, 3, '2022-05-24', '5 to 6.30 pm', 'jaya sharma', 1),
(7, 4, '2022-07-25', '5 to 6 pm', 'neeta', 1),
(4, 5, '2022-12-09', '3.00 pm', 'ram sir', 1);

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `srno` int(11) NOT NULL,
  `name` varchar(40) NOT NULL,
  `mno` bigint(10) NOT NULL,
  `emailid` varchar(40) NOT NULL,
  `message` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`srno`, `name`, `mno`, `emailid`, `message`) VALUES
(2, 'jaya', 9827285963, 'jaya@gmail.com', '123');

-- --------------------------------------------------------

--
-- Table structure for table `course`
--

CREATE TABLE `course` (
  `courseid` int(11) NOT NULL,
  `coursenm` varchar(20) NOT NULL,
  `duration` int(11) NOT NULL,
  `fees` int(11) NOT NULL,
  `coursedetail` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `course`
--

INSERT INTO `course` (`courseid`, `coursenm`, `duration`, `fees`, `coursedetail`) VALUES
(1, 'boxing', 36, 2000, 'fdsfdsdfsdfkldsfl'),
(2, 'salsa', 60, 5000, 'df dflds'),
(3, 'break dance', 30, 2000, 'na'),
(4, 'painting', 15, 1500, 'na'),
(5, 'swimming', 60, 1200, 'na'),
(6, 'sketing', 60, 1500, 'na'),
(7, 'art n crft new ', 30, 1500, 'na');

-- --------------------------------------------------------

--
-- Table structure for table `mstuser`
--

CREATE TABLE `mstuser` (
  `fnm` varchar(40) NOT NULL,
  `mno` bigint(10) NOT NULL,
  `emailid` varchar(40) NOT NULL,
  `pwd` varchar(15) NOT NULL,
  `role` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `mstuser`
--

INSERT INTO `mstuser` (`fnm`, `mno`, `emailid`, `pwd`, `role`) VALUES
('admin', 9425021210, 'admin@gmail.com', '123', 'admin'),
('ayaansh jain', 9827285740, 'ayu@gmail.com', '12345', 'student'),
('deepak', 9425012340, 'deepak@gmail.com', '123', 'student'),
('kavita verma', 9425012345, 'kavita@gmail.com', '123', 'student'),
('meeta', 9827285741, 'meeta1@gmail.com', '123', 'student'),
('monu', 9109715575, 'monusenb93@gmail.com', '4321', 'student'),
('neha jain', 9827285741, 'neha1@gmail.com', '123', 'student'),
('nidhi', 9425085623, 'nidhi@gmail.com', '123', 'student'),
('pihu', 94250458578, 'pihu@gmail.com', '123', 'student'),
('ritu', 9425012345, 'ritu@gmail.com', '123', 'student'),
('xyz', 9425014257, 'xyz@gmail.com', '123', 'student');

-- --------------------------------------------------------

--
-- Table structure for table `test`
--

CREATE TABLE `test` (
  `id` int(11) NOT NULL,
  `name` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `test`
--

INSERT INTO `test` (`id`, `name`) VALUES
(1, 'ram');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admission`
--
ALTER TABLE `admission`
  ADD PRIMARY KEY (`admissionno`);

--
-- Indexes for table `batch1`
--
ALTER TABLE `batch1`
  ADD PRIMARY KEY (`batchid`),
  ADD KEY `courseid` (`courseid`);

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`srno`);

--
-- Indexes for table `course`
--
ALTER TABLE `course`
  ADD PRIMARY KEY (`courseid`);

--
-- Indexes for table `mstuser`
--
ALTER TABLE `mstuser`
  ADD PRIMARY KEY (`emailid`);

--
-- Indexes for table `test`
--
ALTER TABLE `test`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admission`
--
ALTER TABLE `admission`
  MODIFY `admissionno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `batch1`
--
ALTER TABLE `batch1`
  MODIFY `batchid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `srno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `course`
--
ALTER TABLE `course`
  MODIFY `courseid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `batch1`
--
ALTER TABLE `batch1`
  ADD CONSTRAINT `batch1_ibfk_1` FOREIGN KEY (`courseid`) REFERENCES `course` (`courseid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
