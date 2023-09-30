"use client";

import { Button, TextField } from "@mui/material";
import { addCategory } from "@/app/actions/Category";
import { useState } from "react";

export default function AddCategoryForm() {
  const [categoryName, setCategoryName] = useState("");
  const [disabled, setDisabled] = useState(false);
  const onSubmit = (e) => {
    e.preventDefault();
    setDisabled(true);

    const newCategory = {
      name: categoryName,
    };
    addCategory(newCategory).then(() => {
      setDisabled(false);
      setCategoryName("");
    });
  };

  return (
    <form onSubmit={onSubmit} className="mb-3">
      <TextField
        size="small"
        className="mr-3"
        label="Name"
        name="name"
        value={categoryName}
        onChange={(e) => setCategoryName(e.target.value)}
      ></TextField>
      <Button type="submit" variant="contained" disabled={disabled}>
        Submit
      </Button>
    </form>
  );
}
