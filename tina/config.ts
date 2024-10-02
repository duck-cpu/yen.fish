import { defineConfig } from 'tinacms'

export default defineConfig({
  branch: 'main', // Replace with your Git branch
  clientId: process.env.TINA_CLIENT_ID, // Get this from the Tina dashboard
  token: process.env.TINA_TOKEN, // Get this from the Tina dashboard
  build: {
    publicFolder: "public",
    outputFolder: "admin",
  },
  schema: {
    collections: [
      {
        name: "post",
        label: "Blog Posts",
        path: "_posts", // Path where your blog posts are stored
        fields: [
          {
            type: "string",
            name: "title",
            label: "Title",
            required: true,
          },
          {
            type: "datetime",
            name: "date",
            label: "Publish Date",
          },
          {
            type: "rich-text",
            name: "body",
            label: "Body",
          },
        ],
      },
    ],
  },
})
