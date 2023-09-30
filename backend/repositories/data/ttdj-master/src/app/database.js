import { PrismaClient } from "@prisma/client";

global.prisma = global.prisma || new PrismaClient();
const prisma = global.prisma;

export default prisma;
