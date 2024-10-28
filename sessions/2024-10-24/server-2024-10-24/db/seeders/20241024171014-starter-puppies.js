"use strict";

const { Puppy } = require("../models");

const seeds = [
  { name: "apples", ownerId: 1 },
  { name: "ralph", ownerId: 2 },
  { name: "goob", ownerId: 3 },
];

/** @type {import('sequelize-cli').Migration} */
module.exports = {
  async up(queryInterface, Sequelize) {
    /**
     * Add seed commands here.
     *
     * Example:
     * await queryInterface.bulkInsert('People', [{
     *   name: 'John Doe',
     *   isBetaMember: false
     * }], {});
     */
    await Puppy.bulkCreate(seeds);
  },

  async down(queryInterface, Sequelize) {
    /**
     * Add commands to revert seed here.
     *
     * Example:
     * await queryInterface.bulkDelete('People', null, {});
     */
    await queryInterface.bulkDelete("Puppies", {
      name: seeds.map((seed) => seed.name),
    });
  },
};
