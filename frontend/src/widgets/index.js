import FormGroupInput from "./forms/formGroupInput";

import DropDown from "./pickers/Dropdown";
import PaperTable from "./dataviewers/PaperTable";
import Button from "./buttons/Button";

import Card from "./cards/Card";
import ChartCard from "./cards/ChartCard";
import StatsCard from "./cards/StatsCard";

import SidebarPlugin from "./layouts/SidebarPlugin/index";
import ActionPanel from "./layouts/ActionPanel";


let widgets = {
  ActionPanel,
  FormGroupInput,
  Card,
  ChartCard,
  StatsCard,
  PaperTable,
  DropDown,
  SidebarPlugin
};

export default widgets;

export {
  ActionPanel,
  FormGroupInput,
  Card,
  ChartCard,
  StatsCard,
  PaperTable,
  DropDown,
  Button,
  SidebarPlugin
};
