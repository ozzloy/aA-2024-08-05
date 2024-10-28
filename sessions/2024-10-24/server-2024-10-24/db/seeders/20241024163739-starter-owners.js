"use strict";

const { Owner } = require("../models");

const seeds = [
  { name: "Laura" },
  { name: "Bob" },
  { name: "Jill" },
  { name: "Jet" },
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
    await Owner.bulkCreate(seeds);
  },

  async down(queryInterface, Sequelize) {
    /**
     * Add commands to revert seed here.
     *
     * Example:
     * await queryInterface.bulkDelete('People', null, {});
     */
    await queryInterface.bulkDelete("Owners", {
      name: seeds.map((seed) => seed.name),
    });
  },
};
