require("dotenv").config();
const express = require("express");
const app = express();

const PORT = 3000;

// middleware
app.use(express.json());

// routes import
const stateRoutes = require("./routes/stateRoutes");

// routes use
app.use("/api/v1/states", stateRoutes);

// test route
app.get("/", (req, res) => {
res.send("API is running 🚀");
});

app.listen(PORT, () => {
console.log(`Server running on port ${PORT}`);
});
const districtRoutes = require("./routes/districtRoutes");

app.use("/api/v1/districts", districtRoutes);
const subDistrictRoutes = require("./routes/subDistrictRoutes");

app.use("/api/v1/subdistricts", subDistrictRoutes);
const villageRoutes = require("./routes/villageRoutes");

app.use("/api/v1/villages", villageRoutes);
const searchRoutes = require("./routes/searchRoutes");

app.use("/api/v1/search", searchRoutes);
