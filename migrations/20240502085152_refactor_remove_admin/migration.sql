/*
  Warnings:

  - You are about to drop the column `admin_id` on the `Account` table. All the data in the column will be lost.
  - You are about to drop the `Admin` table. If the table is not empty, all the data it contains will be lost.

*/
-- DropForeignKey
ALTER TABLE `Account` DROP FOREIGN KEY `Account_admin_id_fkey`;

-- AlterTable
ALTER TABLE `Account` DROP COLUMN `admin_id`;

-- DropTable
DROP TABLE `Admin`;
