-- phpMyAdmin SQL Dump
-- version 4.6.6deb1+deb.cihar.com~xenial.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jun 07, 2017 at 10:48 PM
-- Server version: 5.7.18
-- PHP Version: 7.0.15-0ubuntu0.16.04.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Courses_Exam`
--

-- --------------------------------------------------------

--
-- Table structure for table `Answers`
--

CREATE TABLE `Answers` (
  `id` int(11) NOT NULL,
  `question_id` int(11) NOT NULL,
  `answer_text` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Answers`
--

INSERT INTO `Answers` (`id`, `question_id`, `answer_text`) VALUES
(73, 26, 'bcvnbmn,.'),
(74, 26, 'bvnb'),
(75, 26, 'hh'),
(76, 27, 'dcfvgbhnjmk'),
(77, 27, 'fdgfhjkk'),
(78, 27, 'bghjkl'),
(139, 48, 'languge programming'),
(140, 48, 'b'),
(141, 48, 'no one'),
(142, 49, 'language programming'),
(143, 49, 'vcvbnm,.'),
(144, 49, 'no one'),
(181, 62, 'languge programming'),
(182, 62, 'scripting'),
(183, 62, 'no one'),
(184, 63, 'language programming'),
(185, 63, 'scripting lang'),
(186, 63, 'cc'),
(187, 64, 'hee tan mal lan'),
(188, 64, 'hyper text mark lang'),
(189, 64, 'hyper text mark up language'),
(190, 65, 'asdfghjk'),
(191, 65, 'vbnm,'),
(192, 65, 'ccvbnm,'),
(193, 66, 'languge programming'),
(194, 66, 'scripting'),
(195, 66, 'no one'),
(196, 67, 'language programming'),
(197, 67, 'scripting lang'),
(198, 67, 'no one'),
(199, 68, 'hee tan mal lan'),
(200, 68, 'hyper text mark lang'),
(201, 68, 'hyper text mark up language'),
(202, 69, 'asdfghjk'),
(203, 69, 'bvnm,.'),
(204, 69, 'ccvbnm,'),
(205, 70, 'vbnm,./'),
(206, 70, 'qwertyu'),
(207, 70, 'fghjkl'),
(208, 71, 'fgvhjkl'),
(209, 71, 'dfcgvhbkjll'),
(210, 71, 'fcgvhbnkm,'),
(211, 72, 'vcbvnbmn,'),
(212, 72, 'vb,jhmngb'),
(213, 72, 'kjkhjgf'),
(214, 73, '.,mnbv'),
(215, 73, '.,mnbv'),
(216, 73, '.kj,mnb'),
(217, 74, 'sdfghj'),
(218, 74, 'cxvbnmm'),
(219, 74, 'jhngbv'),
(220, 75, 'xcvbnmnm'),
(221, 75, 'zxcvbnm,'),
(222, 75, 'xcvbnmm'),
(223, 76, 'xccvbnnm'),
(224, 76, 'vbnm,'),
(225, 76, 'sfdgfhgjj'),
(226, 77, 'cbvnbnm'),
(227, 77, 'sdfghj'),
(228, 77, 'qwertyu');

-- --------------------------------------------------------

--
-- Table structure for table `Chapters`
--

CREATE TABLE `Chapters` (
  `id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `chapter_num` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Chapters`
--

INSERT INTO `Chapters` (`id`, `course_id`, `chapter_num`) VALUES
(12, 7, 3),
(22, 1, 1),
(28, 1, 4),
(29, 1, 5);

-- --------------------------------------------------------

--
-- Table structure for table `correctAnswer`
--

CREATE TABLE `correctAnswer` (
  `question_id` int(11) NOT NULL,
  `correct_ans_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `correctAnswer`
--

INSERT INTO `correctAnswer` (`question_id`, `correct_ans_id`) VALUES
(26, 74),
(27, 78),
(48, 141),
(49, 144),
(62, 181),
(63, 184),
(64, 188),
(65, 192),
(66, 195),
(67, 196),
(68, 199),
(69, 204),
(70, 206),
(71, 209),
(72, 213),
(73, 216),
(74, 219),
(75, 221),
(76, 224),
(77, 228);

-- --------------------------------------------------------

--
-- Table structure for table `Courses`
--

CREATE TABLE `Courses` (
  `id` int(11) NOT NULL,
  `course_name` varchar(150) NOT NULL,
  `chapter_nums` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Courses`
--

INSERT INTO `Courses` (`id`, `course_name`, `chapter_nums`) VALUES
(1, 'java', 5),
(7, 'nodejs', 3);

-- --------------------------------------------------------

--
-- Table structure for table `Questions`
--

CREATE TABLE `Questions` (
  `id` int(11) NOT NULL,
  `quetion` text NOT NULL,
  `chapter_id` int(11) NOT NULL,
  `objective` varchar(200) NOT NULL,
  `level` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Questions`
--

INSERT INTO `Questions` (`id`, `quetion`, `chapter_id`, `objective`, `level`) VALUES
(26, '112345', 12, 'understand', 'simple'),
(27, 'asdfghjkl', 12, 'reminding', 'difficult'),
(48, 'what is python', 22, 'reminding', 'difficult'),
(49, '22222222222', 22, 'understand', 'simple'),
(62, 'aaaaaaaaaa', 28, 'reminding', 'difficult'),
(63, 'what is java script', 28, 'reminding', 'difficult'),
(64, 'asdfghj', 28, 'reminding', 'simple'),
(65, 'asdfghjk', 28, 'reminding', 'simple'),
(66, 'what is python', 29, 'reminding', 'difficult'),
(67, 'what is java script', 29, 'understand', 'difficult'),
(68, 'html', 29, 'creativity', 'difficult'),
(69, 'asdfghjk', 29, 'reminding', 'difficult'),
(70, 'asdfghj', 29, 'understand', 'difficult'),
(71, 'asdfghjk', 29, 'creativity', 'difficult'),
(72, 'bmbcvxbcvnbmn,', 29, 'reminding', 'simple'),
(73, 'm,mhngbfvd', 29, 'reminding', 'simple'),
(74, 'asdfghjk', 29, 'understand', 'simple'),
(75, 'asdfghjk', 29, 'understand', 'simple'),
(76, 'zcxvbnnm', 29, 'creativity', 'simple'),
(77, 'sdfgghjk', 29, 'creativity', 'simple');

-- --------------------------------------------------------

--
-- Table structure for table `Users`
--

CREATE TABLE `Users` (
  `id` int(11) NOT NULL,
  `user_name` varchar(200) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Users`
--

INSERT INTO `Users` (`id`, `user_name`, `email`, `password`) VALUES
(4, 'admin', 'admin@admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `UsersGrades`
--

CREATE TABLE `UsersGrades` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `grade` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Answers`
--
ALTER TABLE `Answers`
  ADD PRIMARY KEY (`id`),
  ADD KEY `question_id` (`question_id`);

--
-- Indexes for table `Chapters`
--
ALTER TABLE `Chapters`
  ADD PRIMARY KEY (`id`),
  ADD KEY `course_id` (`course_id`);

--
-- Indexes for table `correctAnswer`
--
ALTER TABLE `correctAnswer`
  ADD PRIMARY KEY (`question_id`,`correct_ans_id`),
  ADD KEY `correct_ans_id` (`correct_ans_id`);

--
-- Indexes for table `Courses`
--
ALTER TABLE `Courses`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `course_name` (`course_name`);

--
-- Indexes for table `Questions`
--
ALTER TABLE `Questions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `chapter_id` (`chapter_id`);

--
-- Indexes for table `Users`
--
ALTER TABLE `Users`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `UsersGrades`
--
ALTER TABLE `UsersGrades`
  ADD PRIMARY KEY (`id`),
  ADD KEY `course_id` (`course_id`),
  ADD KEY `user_id` (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Answers`
--
ALTER TABLE `Answers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=229;
--
-- AUTO_INCREMENT for table `Chapters`
--
ALTER TABLE `Chapters`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;
--
-- AUTO_INCREMENT for table `Courses`
--
ALTER TABLE `Courses`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT for table `Questions`
--
ALTER TABLE `Questions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=78;
--
-- AUTO_INCREMENT for table `Users`
--
ALTER TABLE `Users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `UsersGrades`
--
ALTER TABLE `UsersGrades`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `Answers`
--
ALTER TABLE `Answers`
  ADD CONSTRAINT `Answers_ibfk_1` FOREIGN KEY (`question_id`) REFERENCES `Questions` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Chapters`
--
ALTER TABLE `Chapters`
  ADD CONSTRAINT `Chapters_ibfk_1` FOREIGN KEY (`course_id`) REFERENCES `Courses` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `correctAnswer`
--
ALTER TABLE `correctAnswer`
  ADD CONSTRAINT `correctAnswer_ibfk_1` FOREIGN KEY (`question_id`) REFERENCES `Questions` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `correctAnswer_ibfk_2` FOREIGN KEY (`correct_ans_id`) REFERENCES `Answers` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Questions`
--
ALTER TABLE `Questions`
  ADD CONSTRAINT `Questions_ibfk_1` FOREIGN KEY (`chapter_id`) REFERENCES `Chapters` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `UsersGrades`
--
ALTER TABLE `UsersGrades`
  ADD CONSTRAINT `UsersGrades_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `Users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `UsersGrades_ibfk_2` FOREIGN KEY (`course_id`) REFERENCES `Courses` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
