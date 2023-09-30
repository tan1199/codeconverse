"use client";

import { deleteCategory } from "@/app/actions/Category";
import { deleteVideo } from "@/app/actions/Video";
import { Button } from "@mui/material";

export default function CategoryList({
  categories,
  setToUpdateCategory,
  setToUpdateVideo,
}) {
  return (
    <ul>
      {categories.map((category) => (
        <li key={category.id}>
          <span className="mr-3">{category.name}</span>
          <Button
            size="small"
            variant="text"
            color="primary"
            onClick={() => setToUpdateCategory(category)}
          >
            Update
          </Button>
          <Button
            size="small"
            variant="text"
            color="primary"
            onClick={() => deleteCategory(category.id)}
          >
            Delete
          </Button>
          <ul>
            {category.videos.map((video) => (
              <li key={video.id}>
                <span className="mr-3">
                  {video.name}, {video.url}
                </span>
                <Button
                  size="small"
                  variant="text"
                  color="primary"
                  onClick={() => setToUpdateVideo(video)}
                >
                  Update
                </Button>
                <Button
                  size="small"
                  variant="text"
                  color="primary"
                  onClick={() => deleteVideo(video.id)}
                >
                  Delete
                </Button>
              </li>
            ))}
          </ul>
        </li>
      ))}
    </ul>
  );
}
