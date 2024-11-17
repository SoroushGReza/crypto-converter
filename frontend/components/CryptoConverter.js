import React, { useState, useEffect } from "react";
import {
  View,
  Text,
  TextInput,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  Image,
  SafeAreaView,
  Linking,
} from "react-native";
import Icon from "react-native-vector-icons/FontAwesome";
import { Picker } from "@react-native-picker/picker";
import axios from "axios";

const CryptoConverter = () => {
  const [cryptos, setCryptos] = useState([]);
  const [crypto, setCrypto] = useState("");
  const [amount, setAmount] = useState("");
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  // Fetch cryptocurrency list
  useEffect(() => {
    const fetchCryptos = async () => {
      try {
        const response = await axios.get(
          "https://crypto-converter-app-372f4b2b2eda.herokuapp.com/api/cryptos/"
        );
        const updatedCryptos = response.data.map((crypto) => ({
          ...crypto,
          icon: getCryptoIcon(crypto.symbol),
        }));
        setCryptos(updatedCryptos);
      } catch (err) {
        console.log("Error fetching cryptocurrencies:", err);
        setError("Failed to load cryptocurrencies. Please try again later.");
      }
    };
    fetchCryptos();
  }, []);

  const fetchConversion = async () => {
    try {
      setError("");
      const response = await axios.get(
        `https://crypto-converter-app-372f4b2b2eda.herokuapp.com/api/convert/${crypto}?amount=${amount}`
      );
      setResult(response.data);
    } catch (err) {
      console.log("Error fetching conversion:", err);
      setError(
        "Error fetching data. Please check the cryptocurrency or amount."
      );
    }
  };

  const getCryptoIcon = (symbol) => {
    const icons = {
      BTC: "https://cryptologos.cc/logos/bitcoin-btc-logo.png",
      ETH: "https://cryptologos.cc/logos/ethereum-eth-logo.png",
      SOL: "https://cryptologos.cc/logos/solana-sol-logo.png",
      ADA: "https://cryptologos.cc/logos/cardano-ada-logo.png",
      DOGE: "https://cryptologos.cc/logos/dogecoin-doge-logo.png",
    };
    return icons[symbol] || null;
  };

  return (
    <SafeAreaView style={styles.fullScreen}>
      <ScrollView contentContainerStyle={styles.container}>
        {/* Logo */}
        <Image
          source={require("../assets/hero.png")}
          style={styles.heroImage}
        />

        {/* Header Text */}
        <Text style={styles.header}>CryptoConverter</Text>

        {/* Picker Section */}
        <Text style={styles.label}>Select Cryptocurrency:</Text>
        <View style={styles.pickerContainer}>
          <Picker
            selectedValue={crypto}
            onValueChange={(itemValue) => setCrypto(itemValue)}
            style={styles.picker}
          >
            <Picker.Item label="Select a cryptocurrency" value="" />
            {cryptos.map((crypto) => (
              <Picker.Item
                key={crypto.id}
                label={crypto.name}
                value={crypto.symbol}
              />
            ))}
          </Picker>
        </View>

        {/* Selected Crypto Display */}
        {crypto && (
          <View style={styles.cryptoInfo}>
            <Image
              source={{ uri: cryptos.find((c) => c.symbol === crypto).icon }}
              style={styles.icon}
            />
            <Text style={styles.selectedCrypto}>
              Selected: {cryptos.find((c) => c.symbol === crypto).name}
            </Text>
          </View>
        )}

        {/* Amount Input */}
        <Text style={styles.label}>Enter Amount:</Text>
        <TextInput
          style={styles.input}
          value={amount}
          onChangeText={setAmount}
          placeholder="Amount"
          keyboardType="numeric"
        />

        {/* Convert Button */}
        <TouchableOpacity style={styles.button} onPress={fetchConversion}>
          <Text style={styles.buttonText}>Convert</Text>
        </TouchableOpacity>

        {/* Result Display */}
        {result && (
          <View style={styles.result}>
            <Text style={styles.resultText}>USD: {result.usd.toFixed(2)}</Text>
            <Text style={styles.resultText}>EUR: {result.eur.toFixed(2)}</Text>
            <Text style={styles.resultText}>SEK: {result.sek.toFixed(2)}</Text>
          </View>
        )}

        {/* Error Message */}
        {error && <Text style={styles.error}>{error}</Text>}
      </ScrollView>

      <View style={styles.footer}>
        <Text style={styles.footerText}>Made by S. Gholamreza</Text>
        <View style={styles.iconContainer}>
          <TouchableOpacity
            onPress={() => Linking.openURL("https://github.com/SoroushGReza")}
          >
            <Icon name="github" size={24} color="#000" style={styles.icon} />
          </TouchableOpacity>
          <TouchableOpacity
            onPress={() =>
              Linking.openURL("https://www.linkedin.com/in/s-gholamreza/")
            }
          >
            <Icon
              name="linkedin"
              size={24}
              color="#0077B5"
              style={styles.icon}
            />
          </TouchableOpacity>
        </View>
      </View>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  fullScreen: {
    flex: 1,
    backgroundColor: "#fff",
  },
  container: {
    padding: 20,
    backgroundColor: "#fff",
  },
  heroImage: {
    width: "100%",
    height: 130,
    resizeMode: "contain",
    marginBottom: 10,
  },
  header: {
    fontSize: 28,
    fontWeight: "bold",
    textAlign: "center",
    marginBottom: 30,
    color: "#333",
  },
  label: {
    fontSize: 18,
    fontWeight: "bold",
    marginBottom: 8,
  },
  pickerContainer: {
    borderWidth: 1,
    borderColor: "#ccc",
    marginBottom: 16,
    borderRadius: 5,
    overflow: "hidden",
    height: 160,
    backgroundColor: "#f9f9f9",
  },
  picker: {
    height: "100%",
    fontSize: 16,
    paddingHorizontal: 10,
    color: "#333",
  },
  cryptoInfo: {
    flexDirection: "row",
    alignItems: "center",
    marginVertical: 10,
  },
  icon: {
    width: 30,
    height: 30,
    marginRight: 10,
  },
  selectedCrypto: {
    fontSize: 16,
    fontWeight: "bold",
  },
  input: {
    borderWidth: 1,
    borderColor: "#ccc",
    padding: 10,
    marginBottom: 16,
    borderRadius: 5,
  },
  button: {
    backgroundColor: "#1A6906",
    padding: 15,
    borderRadius: 5,
    alignItems: "center",
  },
  buttonText: {
    color: "#fff",
    fontSize: 16,
    fontWeight: "bold",
  },
  result: {
    marginTop: 20,
  },
  resultText: {
    fontSize: 18,
    marginBottom: 8,
  },
  error: {
    color: "red",
    marginTop: 20,
  },
  footer: {
    width: "100%",
    backgroundColor: "#fff",
    padding: 2,
    flexDirection: "column",
    alignItems: "center",
    justifyContent: "center",
    marginTop: 20,
    borderTopWidth: 1,
    borderTopColor: "#ddd",
  },
  footerText: {
    fontSize: 9,
    color: "#333",
    marginBottom: 8,
  },
  iconContainer: {
    flexDirection: "row",
    justifyContent: "center",
    alignItems: "center",
  },
  icon: {
    marginHorizontal: 10,
  },
});

export default CryptoConverter;
