import { useState } from "@lynx-js/react";
import * as Lynx from "@lynx-js/types";
import * as React from "react";

export default function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleUsernameInput = (
    e: Lynx.BaseEvent<"input", { value: string }>
  ) => {
    setUsername(e.detail.value);
  };

  const handlePasswordInput = (
    e: Lynx.BaseEvent<"input", { value: string }>
  ) => {
    setPassword(e.detail.value);
  };

  return (
    <view style={{ alignItems: "center", padding: 20 }}>
      <text style={{ fontSize: 24, marginBottom: 20 }}>Login</text>

      <view style={{ marginBottom: 12, width: "100%" }}>
        <text>Username</text>
        {React.createElement("explorer-input", {
          value: username,
          bindinput: handleUsernameInput,
          placeholder: "Enter your username",
          style: "color:white",
          controlled: true
        })}

      </view>

      <view style={{ marginBottom: 20, width: "100%" }}>
        <text>Password</text>
        {React.createElement("explorer-input", {
          value: password,
          bindinput: handlePasswordInput,
          placeholder: "Enter your Password",
          style: "color:white",
          controlled: true
        })}

      </view>

      <view
        style={{
          backgroundColor: "#f00",
          padding: 10,
          borderRadius: 8,
          width: "100%",
          alignItems: "center",
        }}
        bindtap={() => {
          console.log("Logging in");
          (lynx as any).navigateTo({
            url: "/pages/Home",
            success: () => console.log("Navigation success"),
            fail: (err: any) => console.error("Navigation failed", err),
          });
        }}
      >
        <text style={{ color: "white" }}>Log In</text>
      </view>
    </view>
  );
}
