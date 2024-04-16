const yaml = require("js-yaml")

module.exports = eleventyConfig => {
    eleventyConfig.addPassthroughCopy("static");
    eleventyConfig.ignores.add("LICENSE")
    eleventyConfig.ignores.add("README.md")
    eleventyConfig.addFilter("makeUppercase", (value) => value.toUpperCase())
    eleventyConfig.addFilter("presenters", (authors) => authors.filter((author) => author.presenter))
    eleventyConfig.addFilter("nameList", (items) => {
        return items.reduce((acc, cur, i) => {
            if(i == 0) {
                return cur.name
            } else if(i == items.length - 1) {
                return `${acc} and ${cur.name}`
            } else {
                return `${acc}, `
            }
        }, "")
    })
    eleventyConfig.addFilter("listWithoutAnd", (items) =>
    items.reduce((acc, cur, i) => {
        if(i == 0) {
            return cur
        } else {
            return `${acc}, `
        }
    }))
    eleventyConfig.addDataExtension("yaml", contents => yaml.load(contents))
    return {
        dir: {
            data: "data"
        }
    }
};