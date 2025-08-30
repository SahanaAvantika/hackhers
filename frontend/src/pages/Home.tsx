import { useState } from "@lynx-js/react";

export default function Home() {
  const [videoIndex, setVideoIndex] = useState(0);

  const videos = [
    {
      id: 1,
      username: "@abc",
      caption: "Dancing into the weekend 🕺",
      videoUrl: "https://example.com/video1.mp4",
    },
    {
      id: 2,
      username: "@alex",
      caption: "My trip to the mountains 🏔️",
      videoUrl: "https://example.com/video2.mp4",
    },
  ];

  const currentVideo = videos[videoIndex];

  return (
    <view
      style={{
        flex: 1,
        backgroundColor: "black",
        justifyContent: "center",
        alignItems: "center",
        position: "relative",
      }}
    >
      {/* Background video placeholder */}
      <view
        style={{
          width: "100%",
          height: "100%",
          backgroundColor: "#111",
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        <text style={{ color: "white", fontSize: 16 }}>
          [Video Playing: {currentVideo.username}]
        </text>
      </view>

      {/* Bottom-left overlay with username & caption */}
      <view
        style={{
          position: "absolute",
          bottom: 100,
          left: 20,
        }}
      >
        <text style={{ color: "white", fontWeight: "bold", marginBottom: 4 }}>
          {currentVideo.username}
        </text>
        <text style={{ color: "white" }}>{currentVideo.caption}</text>
      </view>

      {/* Right-side actions */}
      <view
        style={{
          position: "absolute",
          bottom: 100,
          right: 20,
          alignItems: "center",
        }}
      >
        <view style={{ marginBottom: 20 }}>
          <text style={{ color: "white" }}>❤️</text>
        </view>
        <view style={{ marginBottom: 20 }}>
          <text style={{ color: "white" }}>💬</text>
        </view>
        <view>
          <text style={{ color: "white" }}>🔗</text>
        </view>
      </view>

      {/* Bottom tab bar */}
      <view
        style={{
          position: "absolute",
          bottom: 0,
          width: "100%",
          height: 60,
          backgroundColor: "rgba(0,0,0,0.6)",
          flexDirection: "row",
          justifyContent: "space-around",
          alignItems: "center",
        }}
      >
        <text style={{ color: "white" }}>Home</text>
        <text style={{ color: "white" }}>Discover</text>
        <text style={{ color: "white" }}>＋</text>
        <text style={{ color: "white" }}>Inbox</text>
        <text style={{ color: "white" }}>Me</text>
      </view>
    </view>
  );
}
