"use client";

import {
  Button,
  Select,
  TextField,
  MenuItem,
  FormControl,
  InputLabel,
} from "@mui/material";
import { addVideo } from "@/app/actions/Video";
import { useState } from "react";

export default function AddVideoForm({ categories }) {
  const [videoName, setVideoName] = useState("");
  const [videoUrl, setVideoUrl] = useState("");
  const [videoCategory, setVideoCategory] = useState(categories[0].id);
  const [disabled, setDisabled] = useState(false);

  const onCategoryChange = (e) => {
    setVideoCategory(e.target.value);
  };
  const onSubmit = (e) => {
    e.preventDefault();
    setDisabled(true);

    const newVideo = {
      name: videoName,
      url: videoUrl,
      category_id: Number(videoCategory),
    };
    addVideo(newVideo).then(() => {
      setDisabled(false);
      setVideoName("");
      setVideoUrl("");
    });
  };

  return (
    <form onSubmit={onSubmit} className="mb-3">
      <TextField
        size="small"
        className="mr-3"
        label="Name"
        name="name"
        value={videoName}
        onChange={(e) => setVideoName(e.target.value)}
      ></TextField>
      <TextField
        size="small"
        className="mr-3"
        label="URL"
        name="url"
        value={videoUrl}
        onChange={(e) => setVideoUrl(e.target.value)}
      ></TextField>
      <FormControl>
        <InputLabel id="category-label">Category</InputLabel>
        <Select
          labelId="category-label"
          size="small"
          className="mr-3"
          label="Category"
          name="category"
          value={videoCategory}
          onChange={onCategoryChange}
        >
          {categories.map((category) => (
            <MenuItem key={category.id} value={category.id}>
              {category.name}
            </MenuItem>
          ))}
        </Select>
      </FormControl>
      <Button type="submit" variant="contained" disabled={disabled}>
        Submit
      </Button>
    </form>
  );
}
