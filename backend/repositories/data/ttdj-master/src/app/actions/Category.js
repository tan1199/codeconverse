"use server";

import prisma from "@/app/database";
import { revalidatePath } from "next/cache";

export async function addCategory(category, path = "/") {
  console.log(`[+] Adding new category: ${JSON.stringify(category)}`);
  const newCategory = await prisma.categories.create({
    data: category,
  });
  revalidatePath(path);

  return newCategory;
}

export async function updateCategory(category, path = "/") {
  console.log(`[+] Updating category: ${JSON.stringify(category)}`);
  const updatedCategory = await prisma.categories.update({
    where: { id: category.id },
    data: category,
  });
  revalidatePath(path);

  return updatedCategory;
}

export async function deleteCategory(categoryId, path = "/") {
  console.log(`[+] Deleting category: ${categoryId}`);
  const deletedCategory = await prisma.categories.delete({
    where: { id: categoryId },
  });
  revalidatePath(path);

  return deletedCategory;
}
