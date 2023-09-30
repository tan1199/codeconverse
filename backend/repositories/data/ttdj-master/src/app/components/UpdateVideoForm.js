"use client";

import {
  Button,
  FormControl,
  InputLabel,
  MenuItem,
  Select,
  TextField,
} from "@mui/material";
import { updateVideo } from "@/app/actions/Video";
import { useState } from "react";

export default function UpdateVideoForm({
  categories,
  video,
  setToUpdateVideo,
}) {
  const [disabled, setDisabled] = useState(false);
  const onChange = (e) => {
    setToUpdateVideo({ ...video, [e.target.name]: e.target.value });
  };
  const onCategoryChange = (e) => {
    setToUpdateVideo({ ...video, category_id: e.target.value });
  };
  const onSubmit = (e) => {
    e.preventDefault();
    setDisabled(true);

    const updatedVideo = {
      id: Number(video.id),
      name: video.name,
      url: video.url,
      category_id: Number(video.category_id),
    };
    updateVideo(updatedVideo).then(() => {
      setDisabled(false);
      setToUpdateVideo(null);
    });
  };

  return (
    <form onSubmit={onSubmit} className="mb-3">
      <input type="hidden" name="id" value={video ? video.id : ""} />
      <TextField
        size="small"
        className="mr-3"
        label="Name"
        name="name"
        value={video ? video.name : ""}
        onChange={onChange}
      ></TextField>
      <TextField
        size="small"
        className="mr-3"
        label="URL"
        name="url"
        value={video ? video.url : ""}
        onChange={onChange}
      ></TextField>
      <FormControl>
        <InputLabel id="category-label">Category</InputLabel>
        <Select
          labelId="category-label"
          size="small"
          className="mr-3"
          label="Category"
          name="category"
          value={video ? video.category_id : categories[0].id}
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
