// Declaration of Variables
let videoPlayer;
let videoIframe;

try {
    const isInstreamDivExist = document.querySelector("#GFG_AD_InContent_Desktop_728x280");

    // Fetch the video API:
    const url = 'https://apiscript.geeksforgeeks.org/get-post-videos/' + window.post_id + '/';
    fetch(url)
        .then(response => response.json())
        .then(resp => {
            if (resp.length > 0) {
                // Increasing the maxHeight of isInstreamDivExist
                isInstreamDivExist.style.maxHeight = '500px';

                // Create and append the video player iframe
                videoPlayer = createIframe("video.html");
                videoIframe = videoPlayer.querySelector('iframe');

                videoIframe.onload = function () {
                    // Post initial data to iframe
                    videoIframe.contentWindow.postMessage({ resp: resp, inView: false }, '*');

                    // Set up Intersection Observer
                    const observer = new IntersectionObserver((entries) => {
                        entries.forEach(entry => {
                            const inView = entry.isIntersecting && entry.intersectionRatio >= 0.5;
                            videoIframe.contentWindow.postMessage({ inView }, '*');

                            if (inView) {
                                observer.unobserve(videoPlayer);    // Unobserve after the element is sufficiently visible
                            }
                        });
                    }, {
                        threshold: [0.5]  // 50% visibility threshold
                    });
                    observer.observe(videoPlayer);

                    // Add Horizontal Lines above and below the instream DIV
                    const horizontalLine = document.createElement('hr');
                    horizontalLine.style.cssText = `
                        border: 1px solid var(--recommendation-card-border);
                        width: 100%;
                    `;
                    isInstreamDivExist.insertAdjacentElement('beforebegin', horizontalLine);
                    isInstreamDivExist.insertAdjacentElement('afterend', horizontalLine.cloneNode(true));

                    handleVideoTitle(resp);
                };

                // Append iframe to instream Div: "#GFG_AD_InContent_Desktop_728x280"
                isInstreamDivExist.appendChild(videoPlayer);

                if (resp.length > 1) {
                    // Modify instream div's CSS to add playlist along with iframe
                    isInstreamDivExist.style.cssText = `
                        display: flex;
                        justify-content: center;
                        // align-items: center;
                    `
                    createPlaylist(resp);
                }
            }
            else {
                console.info("NO INSTREAM VIDEO FOUND ON THIS PAGE");
                isInstreamDivExist.style.minHeight = '0px';
            }
        })
        .catch(error => {
            console.error('There has been a problem with apiscript fetch operation:', error);
            isInstreamDivExist.style.minHeight = '0px'; // Optional: set minHeight if an error occurs
        });
} catch (error) {
    console.error('Unable to load the Video Player, error occured: ', error);
}

// Create Iframe for Video player
function createIframe(filename) {
    // Create the iframe element
    var iframe = document.createElement('iframe');
    iframe.id = 'video-iframe';
    iframe.src = 'https://cdnads.geeksforgeeks.org/instream/' + filename;
    iframe.width = '640px';
    iframe.height = '380px';
    iframe.referrerPolicy = "origin";
    iframe.frameBorder = '0'; // Optional: Remove border
    iframe.allowFullscreen = true; // Optional: Allow fullscreen

    // Create a container for the iframe
    var container = document.createElement('div');
    container.id = 'video-iframe-container';
    container.style.display = 'flex';
    container.style.flexDirection = 'column';
    container.style.justifyContent = 'center'; // Horizontally center
    container.style.alignItems = 'center'; // Vertically center (if container has height)
    container.style.height = '100%'; // Adjust height as needed

    // Append iframe to container
    container.appendChild(iframe);

    return container;
}

// Create the Playlist
function createPlaylist(resp) {
    const playlistContainer = document.createElement('div');
    playlistContainer.id = 'video-playlist-container';
    playlistContainer.style.cssText = `
        width: 350px;
        height: 360px;
        overflow-y: scroll;
        margin-top: 8px;
    `;
    playlistContainer.classList.add('sleek-scrollbar');

    // Add custom scrollbar styles
    const style = document.createElement('style');
    style.innerHTML = `
        /* Custom scrollbar styles similar to the image */
        .sleek-scrollbar::-webkit-scrollbar {
            width: 6px; /* Narrow scrollbar */
        }

        .sleek-scrollbar::-webkit-scrollbar-track {
            background: transparent; /* Invisible track for a clean look */
        }

        .sleek-scrollbar::-webkit-scrollbar-thumb {
            background-color: rgba(0, 0, 0, 0.3); /* Light greyish thumb with some transparency */
            border-radius: 10px; /* Rounded scrollbar thumb for sleek design */
        }

        .sleek-scrollbar::-webkit-scrollbar-thumb:hover {
            background-color: rgba(0, 0, 0, 0.5); /* Darker on hover for subtle interaction */
        }

        /* Optional: Fallback scrollbar styles for Firefox */
        .sleek-scrollbar {
            scrollbar-width: thin; /* Thin scrollbar */
            scrollbar-color: rgba(0, 0, 0, 0.3) transparent; /* Similar color to match */
        }
    `;

    resp.forEach((videoData) => {
        const playlistVideoTile = addVideoIntoPlaylist(videoData);
        playlistContainer.appendChild(playlistVideoTile);
    });

    document.head.appendChild(style);
    document.body.appendChild(playlistContainer);

    // Add event listener for clicks on the playlist container
    playlistContainer.addEventListener('click', (event) => {
        const tile = event.target.closest('#playlist-video-tile');
        if (tile) {
            const videoData = JSON.parse(tile.getAttribute('data-video-data'));     // Retrieve videoData from a data attribute
            videoIframe.contentWindow.postMessage({ playlist: [videoData], inView: true }, '*');
            handleVideoTitle([videoData])
        }
    });
    isInstreamDivExist.appendChild(playlistContainer);
}

// Create a div for video and appeand in 'video-playlist-conatiner'
function addVideoIntoPlaylist(videoData) {
    const playlistVideoTile = document.createElement('div');
    playlistVideoTile.id = 'playlist-video-tile';
    playlistVideoTile.style.cssText = `
        // background-color: aqua;
        display: flex;
        width: 100%;
        height: 90px;
        border-radius: 12px;
        margin-bottom: 10px;
        cursor: pointer;
    `;
    playlistVideoTile.setAttribute('data-video-data', JSON.stringify(videoData));   // To get the data on Click Event 

    // playlistVideoTile.addEventListener('mouseenter', () => {
    //     playlistVideoTile.style.boxShadow = '5px 5px 15px rgba(0, 0, 0, 0.3)';
    // });

    // playlistVideoTile.addEventListener('mouseleave', () => {
    //     playlistVideoTile.style.boxShadow = 'none';
    // });

    const playlistThumbnail = document.createElement('img');
    playlistThumbnail.src = videoData?.meta?.thumbnail;
    playlistThumbnail.alt = 'Video Thumbnail';
    playlistThumbnail.style.cssText = `
        width: 160px;
        height: 90px;
        border-radius: 12px;
        margin-right: 10px;
    `

    const playlistTitle = document.createElement('h2');
    playlistTitle.innerText = cropText(videoData?.title, 46);
    playlistTitle.style.cssText = `
        font-size: 14px;
        padding: 5px
    `

    // Add thumbnail and title of the video
    playlistVideoTile.appendChild(playlistThumbnail);
    playlistVideoTile.appendChild(playlistTitle);

    return playlistVideoTile;
}

// Add and update the title and course link of the playing video
function handleVideoTitle(resp) {
    const videoIframe = document.getElementById("video-iframe-container");

    // Check if the title container already exists
    let videoInfoContainer = document.getElementById('video-info-container');

    // If it doesn't exist, create it
    if (!videoInfoContainer) {
        videoInfoContainer = document.createElement('div');
        videoInfoContainer.id = "video-info-container";
        videoInfoContainer.style.cssText = `
            display: flex;
            width: 640px;
            padding: 0px 10px;
            align-items: center;
        `;
        videoIframe.insertAdjacentElement('beforeend', videoInfoContainer);
    }

    // Handle Title
    let titleHeading = document.getElementById('video-info-container-title');

    // If the title heading doesn't exist, create it
    if (!titleHeading) {
        titleHeading = document.createElement('h1');
        titleHeading.id = "video-info-container-title";
        titleHeading.style.cssText = `
            text-align: left;
            color: var(--similar-read-title-color);
            font-size: 20px;
            font-family: var(--font-primary);
            width: ${resp[0].course_link ? '80%' : '100%'};
        `;
        videoInfoContainer.appendChild(titleHeading);
    }

    // Update the title text
    titleHeading.innerText = "Video | " + resp[0].title;

    // Handle Course Link
    let courseLink = document.getElementById('video-info-container-course-link');

    if (resp[0].course_link) {
        // If the course link doesn't exist, create it
        if (!courseLink) {
            courseLink = document.createElement('a');
            courseLink.id = "video-info-container-course-link";
            courseLink.target = '_blank';
            courseLink.style.cssText = `
                border: 2px solid var(--recommendation-card-border);
                border-radius: 12px;
                height: 30px;
                display: flex;
                align-items: center;
                justify-content: center;
                cursor: pointer;
                text-decoration: none;
                font-size: 15px;
                font-family: var(--font-secondary);
                width: 20%;
                transition: border-color 0.3s;
            `;

            const linkText = document.createElement('span');
            linkText.innerHTML = 'Visit Course';
            linkText.style.color = 'var(--similar-read-title-color)';
            courseLink.appendChild(linkText);

            videoInfoContainer.appendChild(courseLink);

            // Add hover effect using JavaScript
            courseLink.addEventListener('mouseover', function () {
                linkText.style.color = '#fff';
                courseLink.style.backgroundColor = 'rgba(20, 135, 97, 1)';
            });

            courseLink.addEventListener('mouseout', function () {
                linkText.style.color = 'var(--similar-read-title-color)';
                courseLink.style.backgroundColor = 'transparent';
            });
        }

        // Update the course link href
        courseLink.href = replaceDomain(resp[0].course_link);
    } else if (courseLink) {
        // If the course link exists but there is no course link in resp, remove it
        courseLink.remove();
    }
}


// ********** HELPER FUNCTIONS ********** //

const cropText = (text, textLength) => {
    if (typeof (text) === "string") {
        if (text.length <= textLength) {
            return text;
        }
        text = text.substring(0, textLength) + "...";
        return text;
    }
    if (typeof (text) === "object") {
        text = text.join(", ");
        if (text.length <= textLength) {
            return text;
        }
        text = text.substring(0, textLength);
        text = (text.slice(-1) == "," || text.slice(-1) == " ") ? text : text + "...";
        return text;
    }
};

function replaceDomain(url) {
    try {
        const urlObj = new URL(url);
        const urlPathAndParams = urlObj.pathname + urlObj.search;
        return "https://www.geeksforgeeks.org" + urlPathAndParams;  // Replace course link from 'practice' to 'www'
    } catch (error) {
        console.error('Invalid URL:', error);
        return url;
    }
}
