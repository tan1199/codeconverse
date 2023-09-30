"use client";

import { Button, TextField } from "@mui/material";
import { updateCategory } from "@/app/actions/Category";
import { useState } from "react";

export default function UpdateCategoryForm({ category, setToUpdateCategory }) {
  const [disabled, setDisabled] = useState(false);
  const onChange = (e) => {
    setToUpdateCategory({ ...category, name: e.target.value });
  };
  const onSubmit = (e) => {
    e.preventDefault();
    setDisabled(true);

    const updatedCategory = {
      id: Number(category.id),
      name: e.target.name.value,
    };
    updateCategory(updatedCategory).then(() => {
      setDisabled(false);
      setToUpdateCategory(null);
    });
  };

  return (
    <form onSubmit={onSubmit} className="mb-3">
      <input type="hidden" name="id" value={category ? category.id : ""} />
      <TextField
        size="small"
        className="mr-3"
        label="Name"
        name="name"
        value={category ? category.name : ""}
        onChange={onChange}
      ></TextField>
      <Button type="submit" variant="contained" disabled={disabled}>
        Submit
      </Button>
    </form>
  );
}
