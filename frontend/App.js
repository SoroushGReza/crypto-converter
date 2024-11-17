import React from "react";
import { View, StyleSheet } from "react-native";
import CryptoConverter from "./components/CryptoConverter";

export default function App() {
  return (
    <View style={styles.container}>
      <CryptoConverter />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    padding: 0,
    backgroundColor: "#fff",
  },
});
