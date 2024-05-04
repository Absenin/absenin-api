/*
  Warnings:

  - You are about to drop the column `created_at` on the `Date` table. All the data in the column will be lost.

*/
-- DropIndex
DROP INDEX `Date_date_key` ON `Date`;

-- AlterTable
ALTER TABLE `Date` DROP COLUMN `created_at`;
