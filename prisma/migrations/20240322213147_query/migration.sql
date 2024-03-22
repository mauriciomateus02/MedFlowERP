-- CreateTable
CREATE TABLE "query" (
    "queryID" TEXT NOT NULL,
    "date" TEXT NOT NULL,
    "doctor" TEXT NOT NULL,
    "turno" TEXT NOT NULL,
    "user" TEXT NOT NULL,
    "queryType" TEXT NOT NULL
);

-- CreateIndex
CREATE UNIQUE INDEX "query_queryID_key" ON "query"("queryID");
