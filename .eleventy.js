const yaml = require("js-yaml")

module.exports = eleventyConfig => {
    eleventyConfig.addPassthroughCopy("static");
    eleventyConfig.ignores.add("LICENSE")
    eleventyConfig.ignores.add("README.md")
    eleventyConfig.addFilter("makeUppercase", (value) => value.toUpperCase());
    eleventyConfig.addDataExtension("yaml", contents => yaml.load(contents));
    return {
        dir: {
            data: "data"
        }
    }
};