require("dotenv").config();
const express = require("express");
const app = express();
app.use(express.json());

const { Owner, Puppy } = require("./db/models");

app.get("/owners", async (req, res) => {
  const owners = await Owner.findAll();

  res.json(owners);
});

app.get("/puppies", async (req, res) => {
  const puppies = await Puppy.findAll();

  res.json(puppies);
});

app.get("/puppies/:puppyId", async (req, res) => {
  const { puppyId } = req.params;
  const puppyInfo = await Puppy.findOne({
    where: {
      id: puppyId,
    },
    include: Owner,
  });
  res.json(puppyInfo);
});

// right now, this route will not fire because the
//   prior route will get hit first
app.get("/puppies/:id", async (req, res) => {
  const { id } = req.params;
  const puppy = await Puppy.findOne({
    where: { id },
  });

  res.json(puppy);
});

app.post("/owners", async (req, res) => {
  const { name } = req.body;
  console.log("req.body");
  console.log(req.body);
  const owner = Owner.build(req.body);
  await owner.save();
  res.json({ msg: "success", owner });
});

app.post("/puppies/:ownerId", async (req, res) => {
  const { ownerId } = req.params;
  const puppy = Puppy.build(req.body);

  puppy.ownerId = Number(ownerId);
  await puppy.save();

  res.json({ msg: "success", puppy });
});

app.patch("/owners/:id", async (req, res) => {
  const { id } = req.params;
  const { name } = req.body;
  const owner = await Owner.findOne({
    where: { id },
  });
  owner.name = name;

  await owner.save();
  res.json({ msg: "success!", owner });
});

app.patch("/puppies/:puppyId", async (req, res) => {
  const { puppyId } = req.params;
  const { name } = req.body;
  const puppy = await Puppy.findOne({
    where: {
      id: puppyId,
    },
  });
  puppy.name = name;

  await puppy.save();
  res.json({ msg: "success!", puppy });
});

app.delete("/owners/:ownerId", async (req, res) => {
  const { ownerId } = req.params;
  const owner = await Owner.findOne({
    where: {
      id: ownerId,
    },
  });

  await owner.destroy();
  res.json({ msg: "success", owner });
});

app.delete("/puppies/:puppyId", async (req, res) => {
  const { puppyId } = req.params;
  // TODO: rewrite as findByPk
  const puppy = await Puppy.findOne({
    where: {
      id: puppyId,
    },
  });

  if (!puppy) return res.json({ msg: "failed to delete", puppy });

  await puppy.destroy();
  return res.json({ msg: "success", puppy });
});

// get owner from puppy
app.get("/puppy/ownerInfo/:puppyId", async (req, res) => {
  const { puppyId } = req.params;
  const puppy = await Puppy.findByPk(puppyId);
  const owner = await puppy.getOwner();
  res.json(owner);
});

const port = process.env.PORT || 5001;
app.listen(port, () => console.log("server listening on port " + port));
