const yaml = require("js-yaml")

module.exports = eleventyConfig => {
    eleventyConfig.addPassthroughCopy("static");
    eleventyConfig.addDataExtension("yaml", contents => yaml.load(contents));
    return {
        dir: {
            data: "data"
        }
    }
};