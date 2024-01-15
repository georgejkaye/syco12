# syco12

This repo contains the source code for the
[SYCO 12 webpage](https://www.cl.cam.ac.uk/events/syco/12/).
The built HTML files are stored in the
[central SYCO repo](https://github.com/jamievicary/syco/tree/master/12).

## Development

To serve the site at `localhost:8080` and watch for changes, run the following:

```sh
yarn start
```

## Deployment

To build the site into the `_site` directory, run the following:

```sh
yarn build
```

On every push to `main`, the site will be built and deployed to the `/12`
directory in the `jamievicary/syco` repo.
