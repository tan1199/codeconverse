"use server";

import prisma from "@/app/database";
import { revalidatePath } from "next/cache";

export async function addVideo(video, path = "/") {
  console.log(`[+] Adding new video: ${JSON.stringify(video)}`);
  const newVideo = await prisma.videos.create({
    data: video,
  });
  revalidatePath(path);

  return newVideo;
}

export async function updateVideo(video, path = "/") {
  console.log(`[+] Updating video: ${JSON.stringify(video)}`);
  const updatedVideo = await prisma.videos.update({
    where: { id: video.id },
    data: video,
  });
  revalidatePath(path);

  return updatedVideo;
}

export async function deleteVideo(videoId, path = "/") {
  console.log(`[+] Deleting video: ${videoId}`);
  const deletedVideo = await prisma.videos.delete({
    where: { id: videoId },
  });
  revalidatePath(path);

  return deletedVideo;
}
