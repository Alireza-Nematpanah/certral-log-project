
const express = require("express");

const app = express();
const port = 3000;

app.use((req, res, next) => {
  console.log(
    `${new Date().toISOString()} INFO [node-service] ${req.method} ${req.url}`
  );
  next();
});

app.get("/", (req, res) => {
  console.log("Home page requested");
  res.send("Node.js Express service is running!");
});

app.get("/health", (req, res) => {
  res.json({ status: "healthy", service: "node" });
});

app.get("/error", (req, res) => {
  console.error("CENTRAL_LOG_TEST Node.js test error");
  res.status(500).json({
    error: "Test error logged",
    service: "node"
  });
});

app.listen(port, "0.0.0.0", () => {
  console.log(`Node.js service listening on port ${port}`);
});
