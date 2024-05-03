/*
  Warnings:

  - A unique constraint covering the columns `[ip_address]` on the table `Attendance` will be added. If there are existing duplicate values, this will fail.
  - Added the required column `ip_address` to the `Attendance` table without a default value. This is not possible if the table is not empty.

*/
-- AlterTable
ALTER TABLE `Attendance` ADD COLUMN `ip_address` VARCHAR(191) NOT NULL;

-- CreateIndex
CREATE UNIQUE INDEX `Attendance_ip_address_key` ON `Attendance`(`ip_address`);
