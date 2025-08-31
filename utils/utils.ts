import { type ClassValue, clsx } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

export interface Club {
  club_name: string;
  club_presidents: string;
  start_after_sing: boolean;
  room_number: string;
  club_adviser: string;
  meeting_day: string;
  meeting_frequency: string;
  categories: string[];
  description: string;
  logo_link: string;
  alt_text: string;
}

export function createDefaultClub(): Club {
  return {
    club_name: "",
    club_presidents: "",
    start_after_sing: false,
    room_number: "",
    club_adviser: "",
    meeting_day: "",
    meeting_frequency: "",
    categories: [],
    description: "",
    logo_link: "",
    alt_text: "",
  };
}
