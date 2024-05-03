/*
  Warnings:

  - A unique constraint covering the columns `[visitor_identifier]` on the table `Attendance` will be added. If there are existing duplicate values, this will fail.
  - Added the required column `visitor_identifier` to the `Attendance` table without a default value. This is not possible if the table is not empty.

*/
-- AlterTable
ALTER TABLE `Attendance` ADD COLUMN `visitor_identifier` VARCHAR(191) NOT NULL;

-- CreateIndex
CREATE UNIQUE INDEX `Attendance_visitor_identifier_key` ON `Attendance`(`visitor_identifier`);
