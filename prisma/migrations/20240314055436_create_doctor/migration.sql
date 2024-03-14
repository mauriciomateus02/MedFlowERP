-- CreateTable
CREATE TABLE "doctor" (
    "crm" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "phone" TEXT NOT NULL,
    "birthDate" TEXT NOT NULL,
    "password" TEXT NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "doctor_pkey" PRIMARY KEY ("crm")
);

-- CreateIndex
CREATE UNIQUE INDEX "doctor_phone_key" ON "doctor"("phone");
