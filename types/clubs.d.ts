declare module "@/public/clubs.json" {
  import type { Club } from "@/utils/utils";
  const clubs: Club[];
  export default clubs;
}

declare module "../public/clubs.json" {
  import type { Club } from "@/utils/utils";
  const clubs: Club[];
  export default clubs;
}
