-- DropForeignKey
ALTER TABLE `Attendance` DROP FOREIGN KEY `Attendance_date_id_fkey`;

-- DropForeignKey
ALTER TABLE `Attendance` DROP FOREIGN KEY `Attendance_user_id_fkey`;

-- DropForeignKey
ALTER TABLE `Date` DROP FOREIGN KEY `Date_account_id_fkey`;

-- DropForeignKey
ALTER TABLE `User` DROP FOREIGN KEY `User_account_id_fkey`;

-- AddForeignKey
ALTER TABLE `Date` ADD CONSTRAINT `Date_account_id_fkey` FOREIGN KEY (`account_id`) REFERENCES `Account`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `Attendance` ADD CONSTRAINT `Attendance_user_id_fkey` FOREIGN KEY (`user_id`) REFERENCES `User`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `Attendance` ADD CONSTRAINT `Attendance_date_id_fkey` FOREIGN KEY (`date_id`) REFERENCES `Date`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `User` ADD CONSTRAINT `User_account_id_fkey` FOREIGN KEY (`account_id`) REFERENCES `Account`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;
