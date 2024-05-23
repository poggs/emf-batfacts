### Building and running

To start the application locally, run:

`docker compose up --build`.

The application will be available at http://localhost:8081/.

### Deployment

Build the image:

`docker build -t batfacts .`

If you're building on an architecture different to the architecture on which you're deploying, use:

`docker build --platform=linux/amd64 -t batfacts .`

Next, push the image to your Docker registry:

`docker push registry.example.com/batfacts`
