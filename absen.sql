-- phpMyAdmin SQL Dump
-- version 4.6.6deb5ubuntu0.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jan 23, 2022 at 07:57 AM
-- Server version: 5.7.36-0ubuntu0.18.04.1
-- PHP Version: 7.2.24-0ubuntu0.18.04.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `absen`
--

-- --------------------------------------------------------

--
-- Table structure for table `active_codes`
--

CREATE TABLE `active_codes` (
  `code` varchar(15) NOT NULL,
  `id_matkul` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `active_codes`
--

INSERT INTO `active_codes` (`code`, `id_matkul`) VALUES
('168018', 1),
('900060', 1),
('422051', 2);

-- --------------------------------------------------------

--
-- Table structure for table `dosen`
--

CREATE TABLE `dosen` (
  `nid` int(8) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `alamat` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `tgl_lahir` varchar(50) NOT NULL,
  `tmpt_lahir` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dosen`
--

INSERT INTO `dosen` (`nid`, `nama`, `alamat`, `email`, `tgl_lahir`, `tmpt_lahir`) VALUES
(202299, 'admin', 'Jogja', 'admin@gmail.com', '20012002', 'Jogja'),
(202300, 'Canggih Puspo', 'Jogja', 'canggih@gmail.com', '05071994', 'Jogja'),
(202301, 'Ledy Elsera', 'Jogja', 'ledy@gmail.com', '23121994', 'Jogja');

-- --------------------------------------------------------

--
-- Table structure for table `kehadiran`
--

CREATE TABLE `kehadiran` (
  `npm` int(7) NOT NULL,
  `id_matkul` int(5) NOT NULL,
  `status` varchar(5) NOT NULL,
  `tgl_absen` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `kehadiran`
--

INSERT INTO `kehadiran` (`npm`, `id_matkul`, `status`, `tgl_absen`) VALUES
(20223, 1, 'H', '15-01-2022 20:19'),
(20223, 2, 'I', '15-01-2022 20:20'),
(20223, 1, 'H', '15-01-2022 20:23'),
(20223, 1, 'A', '15-01-2022 20:26'),
(20227, 1, 'h', '15-01-2022 20:47'),
(20227, 2, 'i', '15-01-2022 20:47'),
(20223, 2, 'H', '17-01-2022 18:33');

-- --------------------------------------------------------

--
-- Table structure for table `mahasiswa`
--

CREATE TABLE `mahasiswa` (
  `npm` int(7) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `alamat` varchar(50) NOT NULL,
  `angkatan` int(4) NOT NULL,
  `email` varchar(50) NOT NULL,
  `tgl_lahir` varchar(50) NOT NULL,
  `tmpt_lahir` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `mahasiswa`
--

INSERT INTO `mahasiswa` (`npm`, `nama`, `alamat`, `angkatan`, `email`, `tgl_lahir`, `tmpt_lahir`) VALUES
(20223, 'jagad raya ramadhan', 'Solo', 2021, 'jagad@gmail.com', '12062003', 'Klaten'),
(20227, 'bagus ardi pratama', 'purbalingga', 2021, 'tsb@gmail.com', '01082003', 'pbg');

-- --------------------------------------------------------

--
-- Table structure for table `matkul`
--

CREATE TABLE `matkul` (
  `id_matkul` int(5) NOT NULL,
  `nid` int(8) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `sks` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `matkul`
--

INSERT INTO `matkul` (`id_matkul`, `nid`, `nama`, `sks`) VALUES
(1, 202300, 'Algoritma Pemrograman', 3),
(2, 202301, 'Pengembangan Web', 2);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `active_codes`
--
ALTER TABLE `active_codes`
  ADD PRIMARY KEY (`code`),
  ADD KEY `id_matkul` (`id_matkul`);

--
-- Indexes for table `dosen`
--
ALTER TABLE `dosen`
  ADD PRIMARY KEY (`nid`);

--
-- Indexes for table `kehadiran`
--
ALTER TABLE `kehadiran`
  ADD KEY `npm` (`npm`),
  ADD KEY `id_matkul` (`id_matkul`);

--
-- Indexes for table `mahasiswa`
--
ALTER TABLE `mahasiswa`
  ADD PRIMARY KEY (`npm`);

--
-- Indexes for table `matkul`
--
ALTER TABLE `matkul`
  ADD PRIMARY KEY (`id_matkul`),
  ADD KEY `nid` (`nid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `dosen`
--
ALTER TABLE `dosen`
  MODIFY `nid` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=202302;
--
-- AUTO_INCREMENT for table `mahasiswa`
--
ALTER TABLE `mahasiswa`
  MODIFY `npm` int(7) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20229;
--
-- AUTO_INCREMENT for table `matkul`
--
ALTER TABLE `matkul`
  MODIFY `id_matkul` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `active_codes`
--
ALTER TABLE `active_codes`
  ADD CONSTRAINT `active_codes_ibfk_1` FOREIGN KEY (`id_matkul`) REFERENCES `matkul` (`id_matkul`) ON DELETE NO ACTION ON UPDATE CASCADE;

--
-- Constraints for table `kehadiran`
--
ALTER TABLE `kehadiran`
  ADD CONSTRAINT `kehadiran_ibfk_1` FOREIGN KEY (`id_matkul`) REFERENCES `matkul` (`id_matkul`) ON DELETE NO ACTION ON UPDATE CASCADE,
  ADD CONSTRAINT `kehadiran_ibfk_2` FOREIGN KEY (`npm`) REFERENCES `mahasiswa` (`npm`) ON DELETE NO ACTION ON UPDATE CASCADE;

--
-- Constraints for table `matkul`
--
ALTER TABLE `matkul`
  ADD CONSTRAINT `matkul_ibfk_1` FOREIGN KEY (`nid`) REFERENCES `dosen` (`nid`) ON DELETE NO ACTION ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
