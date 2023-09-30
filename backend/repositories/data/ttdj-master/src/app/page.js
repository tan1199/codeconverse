import prisma from "./database";

import CategoryManager from "./components/CategoryManager";

export default async function Home() {
  const categories = await prisma.categories.findMany({
    include: { videos: true },
  });

  return (
    <main>
      <CategoryManager categories={categories} />
    </main>
  );
}
