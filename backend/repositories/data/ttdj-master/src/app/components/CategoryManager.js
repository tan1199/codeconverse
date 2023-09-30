"use client";

import { useState } from "react";
import AddCategoryForm from "./AddCategoryForm";
import AddVideoForm from "./AddVideoForm";
import CategoryList from "./CategoryList";
import UpdateCategoryForm from "./UpdateCategoryForm";
import UpdateVideoForm from "./UpdateVideoForm";

export default function CategoryManager({ categories }) {
  const [toUpdateCategory, setToUpdateCategory] = useState(null);
  const [toUpdateVideo, setToUpdateVideo] = useState(null);

  return (
    <>
      <AddCategoryForm />
      <AddVideoForm categories={categories} />
      <UpdateCategoryForm
        category={toUpdateCategory}
        setToUpdateCategory={setToUpdateCategory}
      />
      <UpdateVideoForm
        categories={categories}
        video={toUpdateVideo}
        setToUpdateVideo={setToUpdateVideo}
      />
      <CategoryList
        categories={categories}
        setToUpdateCategory={setToUpdateCategory}
        setToUpdateVideo={setToUpdateVideo}
      />
    </>
  );
}
