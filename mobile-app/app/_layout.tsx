import { GestureHandlerRootView } from "react-native-gesture-handler";
import {Drawer } from 'expo-router/drawer';
import CustomDrawerContent from '../components/customeDrawer';
import { Ionicons } from "@expo/vector-icons";
import { AntDesign } from '@expo/vector-icons';

export default function RootLayout() {
  return (
    <GestureHandlerRootView>
      <Drawer 
        drawerContent={CustomDrawerContent}
        screenOptions={{
          drawerHideStatusBarOnOpen:false

        }}
        >
        <Drawer.Screen 
          name="index"
          options={{
            title:'Code Reader',
            drawerLabel:'Code Reader',
            unmountOnBlur:true,
            drawerIcon:({color ,size})=>(
              <Ionicons name="camera" size={size} color={color}
                />
            )
          }}
          />
        <Drawer.Screen 
          name="about" 
          options={{
            title:'About',
            drawerLabel:'About',
            drawerIcon:({color ,size})=>(
              <Ionicons name="information-circle" size={size} color={color} />
            )
          }}
          />
      </Drawer>
    </GestureHandlerRootView>
  );
}
