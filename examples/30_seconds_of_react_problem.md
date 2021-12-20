#### useUnload (task/1)

```diff
-const useUnload = fn => {
+const useUnload = fn => {
+
+  useEffect(() => {
+    window.addEventListener('beforeunload', fn);
+    return () => {
+      window.removeEventListener('beforeunload', fn);
+    };
+  }, [fn]);
+};
+
+export default useUnload;
```

#### useUnload (task/1)

```diff
-const useUnload = fn => {
+const useUnload = fn => {
+
+  const unload = function() {
+    if (typeof fn === 'function') {
+      fn();
+    }
+  };
+  window.addEventListener('beforeunload', unload);
+  return unload;
+};
+
+export default useUnload;
```

#### useUnload (task/1)

```diff
-const useUnload = fn => {
+const useUnload = fn => {
+
+  if (useCallback) {
+    return useCallback(fn, [])
+  }
+
+  const listener = useRef()
+  listener.current = fn
+
+  useEffect(() => {
+    return () => {
+      window.removeEventListener('beforeunload', listener.current)
+    }
+  }, [])
+
+  useEffect(() => {
+    window.addEventListener('beforeunload', listener.current)
```

#### useUnload (task/1)

```diff
-const useUnload = fn => {
+const useUnload = fn => {
+
+  return useCallback(() => {
+    if (typeof fn === 'function') {
+      fn();
+    }
+  }, [fn]);
+};
+
+const useDocumentTitle = (title: string) => {
+  const { current: initialTitle } = useRef(document.title);
+  useEffect(() => {
+    document.title = title;
+    return () => {
+      document.title = initialTitle;
```

#### useUnload (task/1)

```diff
-const useUnload = fn => {
+const useUnload = fn => {
+
+    const fnName = Symbol(fn.name);
+    window.addEventListener('beforeunload', ev => {
+        if (typeof fn === 'function') {
+            fn();
+        }
+        if (ev.target === window) {
+            ev.returnValue = true;
+        }
+    });
+    return fnName;
+};
+
+export default useUnload;
```

#### useClickOutside (task/2)

```diff
-const useClickOutside = (ref, callback) => {
+const useClickOutside = (ref, callback) => {
+
+  const handleClick = (e) => {
+    if (ref.current && !ref.current.contains(e.target)) {
+      callback();
+    }
+  };
+
+  useEffect(() => {
+    document.addEventListener('click', handleClick);
+
+    return () => {
+      document.removeEventListener('click', handleClick);
+    };
+  });
+};
+
+const DropdownMenu = ({ children
```

#### useClickOutside (task/2)

```diff
-const useClickOutside = (ref, callback) => {
+const useClickOutside = (ref, callback) => {
+
+  const handleClick = event => {
+    if (ref.current && !ref.current.contains(event.target)) {
+      callback();
+    }
+  };
+
+  useEffect(() => {
+    document.addEventListener("mousedown", handleClick);
+    return () => {
+      document.removeEventListener("mousedown", handleClick);
+    };
+  });
+};
+
+const useCheckbox =
```

#### useClickOutside (task/2)

```diff
-const useClickOutside = (ref, callback) => {
+const useClickOutside = (ref, callback) => {
+
+  const handleClick = (e) => {
+    if (ref.current && !ref.current.contains(e.target)) {
+      callback();
+    }
+  };
+
+  useEffect(() => {
+    document.addEventListener('click', handleClick);
+
+    return () => {
+      document.removeEventListener('click', handleClick);
+    };
+  });
+};
+
+const useModal = (initial
```

#### useClickOutside (task/2)

```diff
-const useClickOutside = (ref, callback) => {
+const useClickOutside = (ref, callback) => {
+
+    useEffect(() => {
+        const handleClickOutside = (event) => {
+            if (ref.current && !ref.current.contains(event.target)) {
+                callback();
+            }
+        };
+
+        document.addEventListener('mousedown', handleClickOutside);
+        return () => {
+            document.removeEventListener('mousedown', handleClickOutside);
+        };
+    }, [ref, callback
```

#### useClickOutside (task/2)

```diff
-const useClickOutside = (ref, callback) => {
+const useClickOutside = (ref, callback) => {
+
+    const handleClick = (e) => {
+        if (ref.current && !ref.current.contains(e.target)) {
+            callback();
+        }
+    };
+
+    useEffect(() => {
+        document.addEventListener('click', handleClick);
+
+        return () => {
+            document.removeEventListener('click', handleClick);
+        };
+    });
+};
+
+export default useClickOutside;
```

#### useSessionStorage (task/3)

```diff
-const useSessionStorage = (keyName, defaultValue) => {
+const useSessionStorage = (keyName, defaultValue) => {
+
+  const [value, setValue] = useState(() => {
+    try {
+      const value = JSON.parse(window.sessionStorage.getItem(keyName));
+      if (value) return value;
+      return defaultValue;
+    } catch (error) {
+      return defaultValue;
+    }
+  });
+
+  const setSessionStorage = value => {
+    window.sessionStorage.setItem(keyName, JSON
```

#### useSessionStorage (task/3)

```diff
-const useSessionStorage = (keyName, defaultValue) => {
+const useSessionStorage = (keyName, defaultValue) => {
+
+  const storedValue = sessionStorage.getItem(keyName);
+  if (storedValue) {
+    return JSON.parse(storedValue);
+  }
+  return defaultValue;
+};
+
+export const storeToSessionStorage = (keyName, value) => {
+  if (value) {
+    sessionStorage.setItem(keyName, JSON.stringify(value));
+  }
+};
+
+export const useM
```

#### useSessionStorage (task/3)

```diff
-const useSessionStorage = (keyName, defaultValue) => {
+const useSessionStorage = (keyName, defaultValue) => {
+
+  return {
+    setItem: (value) => {
+      window.sessionStorage.setItem(keyName, JSON.stringify(value));
+    },
+    getItem: () => {
+      return JSON.parse(window.sessionStorage.getItem(keyName) || defaultValue);
+    },
+    removeItem: () => {
+      window.sessionStorage.removeItem(keyName);
+    },
+  };
+};
```

#### useSessionStorage (task/3)

```diff
-const useSessionStorage = (keyName, defaultValue) => {
+const useSessionStorage = (keyName, defaultValue) => {
+
+  const getFromStorage = () => {
+    const item = window.sessionStorage.getItem(keyName);
+    return item ? JSON.parse(item) : defaultValue;
+  };
+
+  const setToStorage = (value) => {
+    window.sessionStorage.setItem(keyName, JSON.stringify(value));
+  };
+
+  return [getFromStorage, setToStorage];
+};
+
+export default useSession
```

#### useSessionStorage (task/3)

```diff
-const useSessionStorage = (keyName, defaultValue) => {
+const useSessionStorage = (keyName, defaultValue) => {
+
+  const [value, setValue] = useState(() => {
+    const value = localStorage.getItem(keyName);
+    return value !== null ? JSON.parse(value) : defaultValue;
+  });
+
+  const setValueStorage = (value) => {
+    setValue(value);
+    localStorage.setItem(keyName, JSON.stringify(value));
+  };
+
+  return [value, setValue
```

#### useTitle (task/4)

```diff
-const useTitle = title => {
+const useTitle = title => {
+
+  useEffect(() => {
+    if (title) {
+      document.title = title;
+    }
+  }, [title]);
+};
+
+export default useTitle;
```

#### useTitle (task/4)

```diff
-const useTitle = title => {
+const useTitle = title => {
+
+  useEffect(() => {
+    document.title = title;
+  }, [title]);
+};
+
+export default useTitle;
```

#### useTitle (task/4)

```diff
-const useTitle = title => {
+const useTitle = title => {
+
+  const [state, setState] = useState(title);
+  const updateTitle = useCallback(
+    newTitle => {
+      setState(newTitle);
+    },
+    [setState]
+  );
+  return [state, updateTitle];
+};
+
+const TitleHooks = () => {
+  const [title, updateTitle] = useTitle('Hello Hooks');
+  useEffect(() => {
+    document
```

#### useTitle (task/4)

```diff
-const useTitle = title => {
+const useTitle = title => {
+
+  const [titleState, setTitle] = useState(title);
+  const updateTitle = title => {
+    setTitle(title);
+    document.title = title;
+  };
+  return [titleState, updateTitle];
+};
+
+export default useTitle;
```

#### useTitle (task/4)

```diff
-const useTitle = title => {
+const useTitle = title => {
+
+  const htmlTitle = useRef(document.title);
+  useEffect(() => {
+    document.title = title;
+    return () => {
+      document.title = htmlTitle.current;
+    };
+  }, [title]);
+};
+
+const Title = ({ title }) => {
+  useTitle(title);
+  return null;
+};
+
+export default Title;
```

#### useEffectOnce (task/5)

```diff
-const useEffectOnce = (callback, when) => {
+const useEffectOnce = (callback, when) => {
+
+    useEffect(callback, [when]);
+};
+
+export default useEffectOnce;
```

#### useEffectOnce (task/5)

```diff
-const useEffectOnce = (callback, when) => {
+const useEffectOnce = (callback, when) => {
+
+  useEffect(callback, [when]);
+};
+
+export default useEffectOnce;
```

#### useEffectOnce (task/5)

```diff
-const useEffectOnce = (callback, when) => {
+const useEffectOnce = (callback, when) => {
+
+  const ran = useRef(false);
+  useEffect(() => {
+    if (ran.current) return;
+    ran.current = true;
+    return callback();
+  }, when);
+};
+
+const useMappedState = (mapState, mapActions) => {
+  const store = useContext(context);
+  const state = useCallback(mapState(store.state), [store.state]);
+  const
```

#### useEffectOnce (task/5)

```diff
-const useEffectOnce = (callback, when) => {
+const useEffectOnce = (callback, when) => {
+
+  useEffect(callback, [], when);
+};
+
+export const useToggle = (
+  initialValue = false,
+  defaultValue = initialValue
+) => {
+  const [value, setValue] = useState(defaultValue);
+  const toggle = () => setValue(!value);
+  return [value, toggle];
+};
+
+export const useLocalStorage = (
+  key,
+  initialValue = null,
```

#### useEffectOnce (task/5)

```diff
-const useEffectOnce = (callback, when) => {
+const useEffectOnce = (callback, when) => {
+
+  useEffect(callback, [when]);
+};
+
+export const useWindowSize = () => {
+  const [windowSize, setWindowSize] = useState({
+    width: window.innerWidth,
+    height: window.innerHeight,
+  });
+
+  useEffectOnce(() => {
+    const handleResize = () => {
+      setWindowSize({
+        width: window.innerWidth,
+        height: window.
```

#### Accordion (task/6)

```diff
-const AccordionItem = ({ label, isCollapsed, handleClick, children }) => {
+const AccordionItem = ({ label, isCollapsed, handleClick, children }) => {
+
+  const [collapsed, setCollapsed] = useState(isCollapsed);
+
+  const toggleCollapsed = () => {
+    setCollapsed(!collapsed);
+    handleClick();
+  };
+
+  return (
+    <div className="accordion__item">
+      <button
+        type="button"
+        className="accordion__title"
+        onClick={toggleCollapsed}
+      >
+       
```

#### Accordion (task/6)

```diff
-const AccordionItem = ({ label, isCollapsed, handleClick, children }) => {
+const AccordionItem = ({ label, isCollapsed, handleClick, children }) => {
+
+  const labelClassName = isCollapsed ? 'active' : '';
+  return (
+    <div className="accordion__item">
+      <div className="accordion__label" onClick={handleClick}>
+        <span className={labelClassName}>{label}</span>
+      </div>
+      <div className="accordion__content">{children}</div>
+    </
```

#### Accordion (task/6)

```diff
-const AccordionItem = ({ label, isCollapsed, handleClick, children }) => {
+const AccordionItem = ({ label, isCollapsed, handleClick, children }) => {
+
+  const [isOpen, setIsOpen] = useState(isCollapsed);
+
+  return (
+    <div className="AccordionItem">
+      <div
+        className="AccordionItem__label"
+        onClick={() => {
+          setIsOpen(!isOpen);
+          handleClick(!isOpen);
+        }}
+      >
+        <span>{label}</span>
+        <span
```

#### Accordion (task/6)

```diff
-const AccordionItem = ({ label, isCollapsed, handleClick, children }) => {
+const AccordionItem = ({ label, isCollapsed, handleClick, children }) => {
+
+  const [isExpanded, setIsExpanded] = useState(!isCollapsed);
+
+  const onClick = () => {
+    setIsExpanded(!isExpanded);
+    handleClick(!isExpanded);
+  };
+
+  return (
+    <div className="accordion__item">
+      <h3
+        className="accordion__title"
+        onClick={onClick}
+       
```

#### Accordion (task/6)

```diff
-const AccordionItem = ({ label, isCollapsed, handleClick, children }) => {
+const AccordionItem = ({ label, isCollapsed, handleClick, children }) => {
+
+  const classes = classNames(
+    "accordion-item",
+    {
+      "accordion-item--open": !isCollapsed,
+      "accordion-item--closed": isCollapsed
+    }
+  );
+
+  return (
+    <div className={classes}>
+      <div className="accordion-item__header" onClick={handleClick}>
+        <div className="
```

#### useIsomporphicEffect (task/7)

```diff
-const useIsomorphicEffect =
+const useIsomorphicEffect =
+ typeof window !== 'undefined' ? useEffect : useLayoutEffect;
+
+export function useEventListener(eventName: string, handler: EventListenerOrEventListenerObject, element: HTMLElement | Window | Document) {
+  useIsomorphicEffect(() => {
+    const eventListener = (event: Event) => handler(event);
+
+    element.addEventListener(eventName, eventListener);
+
+    return () => {
+     
```

#### useIsomporphicEffect (task/7)

```diff
-const useIsomorphicEffect =
+const useIsomorphicEffect =
+ typeof window !== 'undefined' ? useEffect : useLayoutEffect;
+
+function nodeIsContainedWithin(container, child) {
+  let parent = child.parentNode;
+
+  while (parent !== null) {
+    if (parent === container) {
+      return true;
+    }
+
+    parent = parent.parentNode;
+  }
+
+  return false;
+}
+
+function getScrollParent(element) {
+ 
```

#### useIsomporphicEffect (task/7)

```diff
-const useIsomorphicEffect =
+const useIsomorphicEffect =
+ typeof window !== 'undefined' && window.document && window.document.createElement;
+
+function useEventCallback<T extends (...args: any[]) => any>(fn: T): T {
+  const ref = useRef<T>();
+
+  useIsomorphicEffect(() => {
+    ref.current = fn;
+  });
+
+  return useCallback(
+    (...args: Parameters<T>) => {
+      return
```

#### useIsomporphicEffect (task/7)

```diff
-const useIsomorphicEffect =
+const useIsomorphicEffect =
+ typeof window !== 'undefined' ? React.useLayoutEffect : React.useEffect;
+
+interface Props {
+  children: React.ReactNode;
+  isOpen: boolean;
+  onClose: () => void;
+  timeout: number;
+}
+
+const Toast: React.FC<Props> = ({ children, isOpen, onClose, timeout }) => {
+  const containerRef = React.useRef<HTML
```

#### useIsomporphicEffect (task/7)

```diff
-const useIsomorphicEffect =
+const useIsomorphicEffect =
+ typeof window !== 'undefined' ? useEffect : useLayoutEffect;
+
+//
+// https://github.com/gaearon/react-hot-loader/issues/1069
+//
+
+function logTypeError(name: string, err: any) {
+  // @ts-ignore
+  console.error(err);
+}
+
+//
+// https://github.com/gaearon/react-hot-loader/issues
```

#### useGetSet (task/8)

```diff
-const useGetSet = initialState => {
+const useGetSet = initialState => {
+
+  const [state, setState] = useState(initialState);
+
+  return [state, setState];
+};
+
+export default useGetSet;
```

#### useGetSet (task/8)

```diff
-const useGetSet = initialState => {
+const useGetSet = initialState => {
+
+  const [state, setState] = useState(initialState);
+
+  return [state, setState];
+};
+
+export default useGetSet;
```

#### useGetSet (task/8)

```diff
-const useGetSet = initialState => {
+const useGetSet = initialState => {
+
+  const [state, setState] = useState(initialState);
+
+  return [state, setState];
+};
+
+export default useGetSet;
```

#### useGetSet (task/8)

```diff
-const useGetSet = initialState => {
+const useGetSet = initialState => {
+
+  const [state, setState] = useState(initialState);
+
+  return [state, setState];
+};
+
+export default useGetSet;
```

#### useGetSet (task/8)

```diff
-const useGetSet = initialState => {
+const useGetSet = initialState => {
+
+  const [data, setData] = useState(initialState);
+
+  const getData = useCallback(() => data, [data]);
+
+  const setDataFunc = useCallback(value => setData(value), [setData]);
+
+  return [getData, setDataFunc];
+};
+
+export default useGetSet;
```

#### useInterval (task/9)

```diff
-const useInterval = (callback, delay) => {
+const useInterval = (callback, delay) => {
+
+  const savedCallback = useRef();
+
+  // Remember the latest callback.
+  useEffect(() => {
+    savedCallback.current = callback;
+  }, [callback]);
+
+  // Set up the interval.
+  useEffect(() => {
+    function tick() {
+      savedCallback.current();
+    }
+    if (delay !== null) {
+      let id = setInterval(tick, delay);
+      return ()
```

#### useInterval (task/9)

```diff
-const useInterval = (callback, delay) => {
+const useInterval = (callback, delay) => {
+
+  const savedCallback = useRef();
+
+  // Remember the latest callback.
+  useEffect(() => {
+    savedCallback.current = callback;
+  }, [callback]);
+
+  // Set up the interval.
+  useEffect(() => {
+    function tick() {
+      savedCallback.current();
+    }
+    if (delay !== null) {
+      let id = setInterval(tick, delay);
+      return ()
```

#### useInterval (task/9)

```diff
-const useInterval = (callback, delay) => {
+const useInterval = (callback, delay) => {
+
+  const savedCallback = useRef();
+
+  // Remember the latest callback.
+  useEffect(() => {
+    savedCallback.current = callback;
+  }, [callback]);
+
+  // Set up the interval.
+  useEffect(() => {
+    function tick() {
+      savedCallback.current();
+    }
+    if (delay !== null) {
+      let id = setInterval(tick, delay);
+      return ()
```

#### useInterval (task/9)

```diff
-const useInterval = (callback, delay) => {
+const useInterval = (callback, delay) => {
+
+  const savedCallback = useRef();
+
+  // Remember the latest callback.
+  useEffect(() => {
+    savedCallback.current = callback;
+  }, [callback]);
+
+  // Set up the interval.
+  useEffect(() => {
+    function tick() {
+      savedCallback.current();
+    }
+    if (delay !== null) {
+      let id = setInterval(tick, delay);
+      return ()
```

#### useInterval (task/9)

```diff
-const useInterval = (callback, delay) => {
+const useInterval = (callback, delay) => {
+
+    const savedCallback = useRef();
+
+    // Remember the latest callback.
+    useEffect(() => {
+        savedCallback.current = callback;
+    }, [callback]);
+
+    // Set up the interval.
+    useEffect(() => {
+        function tick() {
+            savedCallback.current();
+        }
+        if (delay !== null) {
+            let id = setInterval(tick, delay);
+            return ()
```

#### Loader (task/10)

```diff
-const Loader = ({ size }) => {
+const Loader = ({ size }) => {
+
+  return (
+    <div className="loader">
+      <div className="lds-ring">
+        <div></div>
+        <div></div>
+        <div></div>
+        <div></div>
+      </div>
+    </div>
+  );
+};
+
+export default Loader;
```

#### Loader (task/10)

```diff
-const Loader = ({ size }) => {
+const Loader = ({ size }) => {
+
+  return (
+    <div>
+      <img src={loadingIcon} alt="Loading Icon" className={`loader-${size}`} />
+    </div>
+  );
+};
+
+Loader.propTypes = {
+  size: PropTypes.string
+};
+
+Loader.defaultProps = {
+  size: 'medium'
+};
+
+export default Loader;
```

#### Loader (task/10)

```diff
-const Loader = ({ size }) => {
+const Loader = ({ size }) => {
+
+  return (
+    <div className="loadingio-spinner-double-ring-r64jb2mr8s">
+      <div className="ldio-6tp9m3zq3l">
+        <div></div>
+        <div></div>
+        <div>
+          <div></div>
+        </div>
+        <div>
+          <div></div>
+        </div>
```

#### Loader (task/10)

```diff
-const Loader = ({ size }) => {
+const Loader = ({ size }) => {
+
+  return (
+    <svg
+      width={size}
+      height={size}
+      viewBox="0 0 38 38"
+      xmlns="http://www.w3.org/2000/svg"
+    >
+      <g stroke="none" strokeWidth="1" fill="none" fillRule="evenodd">
+        <g transform="translate(1.000000, 1.000000)" fill="#000000">
+         
```

#### Loader (task/10)

```diff
-const Loader = ({ size }) => {
+const Loader = ({ size }) => {
+
+  return (
+    <LoaderContainer>
+      <LoaderIcon size={size} />
+    </LoaderContainer>
+  );
+};
+
+Loader.propTypes = {
+  size: PropTypes.number,
+};
+
+Loader.defaultProps = {
+  size: 50,
+};
+
+export default Loader;
```

#### Modal (task/11)

```diff
-const Modal = ({ isVisible = false, title, content, footer, onClose }) => {
+const Modal = ({ isVisible = false, title, content, footer, onClose }) => {
+
+  const handleOnClose = () => {
+    onClose()
+  }
+
+  return (
+    <ModalStyle isVisible={isVisible}>
+      <Container>
+        <Header>
+          <Title>{title}</Title>
+          <Close onClick={handleOnClose}>x</Close>
+        </Header>
+        <Content>{content}</Content>
+        <Footer>{footer
```

#### Modal (task/11)

```diff
-const Modal = ({ isVisible = false, title, content, footer, onClose }) => {
+const Modal = ({ isVisible = false, title, content, footer, onClose }) => {
+
+  const handleClick = (event) => {
+    const target = event.target;
+    if (target === event.currentTarget) {
+      onClose();
+    }
+  };
+
+  return (
+    <ModalContainer isVisible={isVisible} onClick={handleClick}>
+      <ModalInner>
+        <div className="modal-header">
+          <span className="modal-title
```

#### Modal (task/11)

```diff
-const Modal = ({ isVisible = false, title, content, footer, onClose }) => {
+const Modal = ({ isVisible = false, title, content, footer, onClose }) => {
+
+  const [isVisibleClassName, setIsVisibleClassName] = useState(
+    isVisible ? 'modal--visible' : ''
+  );
+
+  useEffect(() => {
+    setIsVisibleClassName(isVisible ? 'modal--visible' : '');
+  }, [isVisible]);
+
+  return (
+    <div className={`modal ${isVisibleClassName}`}
```

#### Modal (task/11)

```diff
-const Modal = ({ isVisible = false, title, content, footer, onClose }) => {
+const Modal = ({ isVisible = false, title, content, footer, onClose }) => {
+
+  const classes = useStyles();
+  return (
+    <div className={classes.root}>
+      <ModalDialog isVisible={isVisible} onClose={onClose}>
+        <div className={classes.paper}>
+          <div className={classes.header}>
+            <Typography className={classes.title}>{title}</Typography>
+            <IconButton
+              aria
```

#### Modal (task/11)

```diff
-const Modal = ({ isVisible = false, title, content, footer, onClose }) => {
+const Modal = ({ isVisible = false, title, content, footer, onClose }) => {
+
+  const isContentEmpty = content === null || content === undefined;
+  const hasTitle = title !== null && title !== undefined;
+  const hasFooter = footer !== null && footer !== undefined;
+
+  return (
+    <div className={cx('Modal', { 'Modal--visible': isVisible })}>
+      <div className="Modal__container">
+        <div className="
```

#### useIntersectionObserver (task/12)

```diff
-const useIntersectionObserver = (ref, options) => {
+const useIntersectionObserver = (ref, options) => {
+
+  const [entry, setEntry] = useState(null);
+  const observer = useRef(null);
+
+  useEffect(() => {
+    observer.current = new IntersectionObserver(entries => {
+      setEntry(entries[0]);
+    }, options);
+    if (ref.current) {
+      observer.current.observe(ref.current);
+    }
+    return () => {
+      observer
```

#### useIntersectionObserver (task/12)

```diff
-const useIntersectionObserver = (ref, options) => {
+const useIntersectionObserver = (ref, options) => {
+
+  const [isIntersecting, setIsIntersecting] = useState(false);
+
+  useEffect(() => {
+    const observer = new IntersectionObserver(entries => {
+      const { isIntersecting } = entries[0];
+      setIsIntersecting(isIntersecting);
+    }, options);
+
+    if (ref.current) {
+      observer.observe(ref.current);
+   
```

#### useIntersectionObserver (task/12)

```diff
-const useIntersectionObserver = (ref, options) => {
+const useIntersectionObserver = (ref, options) => {
+
+  const [entry, setEntry] = useState();
+  const [entries, setEntries] = useState();
+  const [{ isIntersecting }, setIsIntersecting] = useState();
+
+  useEffect(() => {
+    const io = new IntersectionObserver(
+      ([entry]) => {
+        setEntry(entry);
+      },
+      options
+    );
+
+    if (ref.current) {
```

#### useIntersectionObserver (task/12)

```diff
-const useIntersectionObserver = (ref, options) => {
+const useIntersectionObserver = (ref, options) => {
+
+  const [entry, setEntry] = useState(null);
+  const [isIntersecting, setIsIntersecting] = useState(false);
+
+  useEffect(() => {
+    const observer = new IntersectionObserver(
+      ([entry]) => {
+        setEntry(entry);
+        setIsIntersecting(entry.isIntersecting);
+      },
+      options
+    );
+
+    observer.obser
```

#### useIntersectionObserver (task/12)

```diff
-const useIntersectionObserver = (ref, options) => {
+const useIntersectionObserver = (ref, options) => {
+
+  const [entry, setEntry] = useState(null);
+  const [node, setNode] = useState(null);
+
+  useEffect(() => {
+    const observer = new IntersectionObserver(entries => {
+      if (entries[0].isIntersecting) {
+        setEntry(entries[0]);
+        setNode(ref.current);
+      }
+    }, options);
+
+    if (
```

#### Slider (task/13)

```diff
-const Slider = ({ 
+const Slider = ({ 
+value, onChange }) => {
+  return (
+    <div className="slider">
+      <SliderTrack>
+        <SliderThumb value={value} onChange={onChange} />
+      </SliderTrack>
+    </div>
+  );
+};
+
+Slider.propTypes = {
+  value: PropTypes.number.isRequired,
+  onChange: PropTypes.func.isRequired,
+};
```

#### Slider (task/13)

```diff
-const Slider = ({ 
+const Slider = ({ 
+x, y, size, onClick, onHover, isSelected, label, value, suffix, onChange }) => {
+  const handleClick = (event) => {
+    if (onClick) {
+      onClick(event);
+    }
+  };
+
+  const handleMouseOver = (event) => {
+    if (onHover) {
+      onHover(event);
+    }
+  };
+
+  const handleMouse
```

#### Slider (task/13)

```diff
-const Slider = ({ 
+const Slider = ({ 
+value, min, max, step, onChange }) => {
+  const [localValue, setLocalValue] = useState(value);
+
+  useEffect(() => {
+    setLocalValue(value);
+  }, [value]);
+
+  const handleChange = (event, newValue) => {
+    setLocalValue(newValue);
+    onChange(newValue);
+  };
+
+  return (
+    <Grid container spacing={2} align
```

#### Slider (task/13)

```diff
-const Slider = ({ 
+const Slider = ({ 
+getPosition, id, label, value, options, setValue }) => {
+  const handleChange = (event, newValue) => {
+    setValue(newValue);
+  };
+
+  return (
+    <Card className="slider-card">
+      <Typography variant="h5" component="h2">
+        {label}
+      </Typography>
+      <Slider
+        min={options.min}
+        max={
```

#### Slider (task/13)

```diff
-const Slider = ({ 
+const Slider = ({ 
+max, onChange, value }) => {
+  const handleChange = (event, newValue) => {
+    onChange(newValue);
+  };
+
+  return (
+    <div>
+      <Slider
+        min={0}
+        max={max}
+        value={value}
+        onChange={handleChange}
+        valueLabelDisplay="auto"
+        marks
+        step={1}
+      />
+    </div>
```

#### useToggler (task/14)

```diff
-const useToggler = initialState => {
+const useToggler = initialState => {
+
+  const [isToggled, setToggled] = useState(initialState);
+
+  const handleToggle = () => {
+    setToggled(prevState => !prevState);
+  };
+
+  return {
+    isToggled,
+    handleToggle
+  };
+};
+
+export default useToggler;
```

#### useToggler (task/14)

```diff
-const useToggler = initialState => {
+const useToggler = initialState => {
+
+	const [isToggled, setToggled] = useState(initialState);
+
+	const toggle = () => setToggled(!isToggled);
+
+	return [isToggled, toggle];
+};
+
+export default useToggler;
```

#### useToggler (task/14)

```diff
-const useToggler = initialState => {
+const useToggler = initialState => {
+
+  const [isOpen, setIsOpen] = useState(initialState);
+
+  const toggle = () => setIsOpen(!isOpen);
+
+  return { isOpen, toggle };
+};
+
+export default useToggler;
```

#### useToggler (task/14)

```diff
-const useToggler = initialState => {
+const useToggler = initialState => {
+
+  const [state, setState] = useState(initialState);
+
+  const toggler = useCallback(() => {
+    setState(currentState => !currentState);
+  }, []);
+
+  return [state, toggler];
+};
+
+export default useToggler;
```

#### useToggler (task/14)

```diff
-const useToggler = initialState => {
+const useToggler = initialState => {
+
+  const [isToggled, setToggled] = useState(initialState);
+
+  const toggle = () => setToggled(!isToggled);
+
+  return [isToggled, toggle];
+};
+
+export default useToggler;
```

#### useHover (task/15)

```diff
-const useHover = () => {
+const useHover = () => {
+
+  const [hover, setHover] = useState(false);
+  const onMouseOver = () => setHover(true);
+  const onMouseOut = () => setHover(false);
+  return { hover, onMouseOver, onMouseOut };
+};
+
+const useAnimation = (duration = 1000) => {
+  const [isAnimated, setAnimated] = useState(false);
+  const animationStyles
```

#### useHover (task/15)

```diff
-const useHover = () => {
+const useHover = () => {
+
+  const [hover, setHover] = useState(false);
+  const ref = useRef(null);
+
+  useEffect(() => {
+    function handleMouseOver() {
+      setHover(true);
+    }
+
+    function handleMouseOut() {
+      setHover(false);
+    }
+
+    ref.current.addEventListener('mouseover', handleMouseOver);
+    ref.current.addEventListener('
```

#### useHover (task/15)

```diff
-const useHover = () => {
+const useHover = () => {
+
+  const [hovered, setHovered] = useState(false);
+
+  const onMouseEnter = () => setHovered(true);
+  const onMouseLeave = () => setHovered(false);
+
+  return {
+    hovered,
+    onMouseEnter,
+    onMouseLeave,
+  };
+};
+
+export default useHover;
```

#### useHover (task/15)

```diff
-const useHover = () => {
+const useHover = () => {
+
+  const [hovered, setHovered] = useState(false);
+  const toggleHover = () => setHovered(!hovered);
+  return { hovered, toggleHover };
+};
+
+export default useHover;
```

#### useHover (task/15)

```diff
-const useHover = () => {
+const useHover = () => {
+
+  const [isHovering, setIsHovering] = useState(false);
+  const ref = useRef(null);
+
+  const handleMouseOver = () => {
+    setIsHovering(true);
+  };
+
+  const handleMouseOut = () => {
+    setIsHovering(false);
+  };
+
+  useEffect(() => {
+    const node = ref.current;
+    if (node
```

#### usePrevious (task/16)

```diff
-const usePrevious = value => {
+const usePrevious = value => {
+
+  const ref = useRef();
+  useEffect(() => {
+    ref.current = value;
+  });
+  return ref.current;
+};
+
+export const useLocalStorage = (
+  key,
+  initialValue,
+  type = 'value',
+  isServer = false
+) => {
+  const [storedValue, setStoredValue] = useState(() => {
+    if (isServer) {
```

#### usePrevious (task/16)

```diff
-const usePrevious = value => {
+const usePrevious = value => {
+
+  const ref = useRef();
+  useEffect(() => {
+    ref.current = value;
+  });
+  return ref.current;
+};
+
+const App: React.FC = () => {
+  const state = useGlobalState();
+  const prevState = usePrevious(state);
+  const updateContent = useCallback(
+    (result: IContent, idx: number) => {
+      const content = [...
```

#### usePrevious (task/16)

```diff
-const usePrevious = value => {
+const usePrevious = value => {
+
+  const ref = useRef();
+  useEffect(() => {
+    ref.current = value;
+  });
+  return ref.current;
+};
+
+export const usePortal = name => {
+  const [isOpen, setIsOpen] = useState(false);
+  const previousName = usePrevious(name);
+  const [state, dispatch] = useReducer(reducer, null);
+
+  useEffect(()
```

#### usePrevious (task/16)

```diff
-const usePrevious = value => {
+const usePrevious = value => {
+
+  const ref = useRef();
+  useEffect(() => {
+    ref.current = value;
+  });
+  return ref.current;
+};
+
+export default usePrevious;
```

#### usePrevious (task/16)

```diff
-const usePrevious = value => {
+const usePrevious = value => {
+
+    const ref = useRef();
+    useEffect(() => {
+        ref.current = value;
+    });
+    return ref.current;
+};
+
+const useSearchState = (initialValue) => {
+    const [search, setSearch] = useState(initialValue);
+    const prevSearch = usePrevious(search);
+
+    useEffect(() => {
+        if (prevSearch !== search) {
+            onSearch
```

#### useMediaQuery (task/17)

```diff
-const useMediaQuery = (query, whenTrue, whenFalse) => {
+const useMediaQuery = (query, whenTrue, whenFalse) => {
+
+    const mql = window.matchMedia(query);
+    let hasMatch = mql.matches;
+    if (hasMatch) {
+        return whenTrue;
+    } else {
+        return whenFalse;
+    }
+};
+
+export const useScreenWidth = () => {
+    const [width, setWidth] = useState(useMediaQuery('(min-width: 500px)', 500, 320));
+    use
```

#### useMediaQuery (task/17)

```diff
-const useMediaQuery = (query, whenTrue, whenFalse) => {
+const useMediaQuery = (query, whenTrue, whenFalse) => {
+
+    const mediaQueryList = window.matchMedia(query);
+    let currentValue = null;
+    const onQueryChange = (event) => {
+        if (event.matches) {
+            currentValue = whenTrue;
+        } else {
+            currentValue = whenFalse;
+        }
+    };
+    onQueryChange(mediaQueryList);
+    return [currentValue, onQueryChange];
+};
+
+export default use
```

#### useMediaQuery (task/17)

```diff
-const useMediaQuery = (query, whenTrue, whenFalse) => {
+const useMediaQuery = (query, whenTrue, whenFalse) => {
+
+  const [matches, setMatches] = useState(
+    window.matchMedia(query).matches
+  );
+
+  useEffect(() => {
+    const handler = e => setMatches(e.matches);
+    window.matchMedia(query).addListener(handler);
+    return () => window.matchMedia(query).removeListener(handler);
+  }, [query]);
+
+  return matches ? whenTrue : when
```

#### useMediaQuery (task/17)

```diff
-const useMediaQuery = (query, whenTrue, whenFalse) => {
+const useMediaQuery = (query, whenTrue, whenFalse) => {
+
+  return useContext(MediaQueryContext) === query ? whenTrue : whenFalse;
+};
+
+const useMediaQueryWithContext = (query, whenTrue, whenFalse) => {
+  return useContext(MediaQueryContext) === query ? whenTrue : whenFalse;
+};
+
+export { useMediaQuery, useMediaQueryWithContext };
```

#### useMediaQuery (task/17)

```diff
-const useMediaQuery = (query, whenTrue, whenFalse) => {
+const useMediaQuery = (query, whenTrue, whenFalse) => {
+
+    const mediaQuery = window.matchMedia(query);
+    if (mediaQuery.matches) {
+        return whenTrue;
+    } else {
+        return whenFalse;
+    }
+};
+
+export default useMediaQuery;
```

#### useDefault (task/18)

```diff
-const useDefault = (defaultState, initialState) => {
+const useDefault = (defaultState, initialState) => {
+
+  const [state, setState] = useState(() =>
+    initialState === undefined ? defaultState : initialState
+  );
+
+  return [state, setState];
+};
+
+export default useDefault;
```

#### useDefault (task/18)

```diff
-const useDefault = (defaultState, initialState) => {
+const useDefault = (defaultState, initialState) => {
+
+    const initialStateIsUndefined = typeof initialState === 'undefined';
+    const isInitialStateDefault = initialState === defaultState;
+    if (initialStateIsUndefined || isInitialStateDefault) {
+        return defaultState;
+    }
+    return initialState;
+};
+const createReducer = (reducers, defaultState) => (state, action) => {
+    if (typeof reducers === 'function')
```

#### useDefault (task/18)

```diff
-const useDefault = (defaultState, initialState) => {
+const useDefault = (defaultState, initialState) => {
+
+    const [state, setState] = useState(() =>
+        initialState === undefined ? defaultState : initialState
+    );
+
+    return [state, setState];
+};
+
+export default useDefault;
```

#### useDefault (task/18)

```diff
-const useDefault = (defaultState, initialState) => {
+const useDefault = (defaultState, initialState) => {
+
+  return (
+    initialState === undefined ? defaultState : initialState
+  );
+};
+
+const useCallbackCondition = (callback, condition) => {
+  return useMemo(() => condition ? callback : null, [condition]);
+};
+
+const useForceUpdate = () => {
+  const [, setTick] = useState(0);
+  const update = useCallback(() => setTick(tick => tick + 1
```

#### useDefault (task/18)

```diff
-const useDefault = (defaultState, initialState) => {
+const useDefault = (defaultState, initialState) => {
+
+  return Object.keys(defaultState).reduce((acc, key) => {
+    if (initialState[key] === undefined) {
+      acc[key] = defaultState[key];
+    } else {
+      acc[key] = initialState[key];
+    }
+    return acc;
+  }, {});
+};
+
+export default useDefault;
```

#### TagInput (task/19)

```diff
-const TagInput = ({ tags }) => {
+const TagInput = ({ tags }) => {
+
+  const [input, setInput] = useState('');
+  const [isTagsListOpen, setIsTagsListOpen] = useState(false);
+  const [filteredTags, setFilteredTags] = useState(tags);
+
+  const searchTags = () => {
+    const searchedTags = tags.filter(tag => tag.toLowerCase().includes(input.toLowerCase()));
+    setFilteredTags(se
```

#### TagInput (task/19)

```diff
-const TagInput = ({ tags }) => {
+const TagInput = ({ tags }) => {
+
+  const [input, setInput] = useState('');
+  const [tagInput, setTagInput] = useState([]);
+
+  const handleChange = (e) => {
+    const { value } = e.target;
+    setInput(value);
+  };
+
+  const handleKeyPress = (e) => {
+    if (e.key === 'Enter') {
+      e.preventDefault();
+      add
```

#### TagInput (task/19)

```diff
-const TagInput = ({ tags }) => {
+const TagInput = ({ tags }) => {
+
+  const [text, setText] = useState('');
+  const [tagsArr, setTagsArr] = useState(tags);
+
+  const handleTextChange = event => {
+    setText(event.target.value);
+  };
+
+  const handleSubmit = event => {
+    event.preventDefault();
+    if (text) {
+      setTagsArr([...tagsArr, text]);
+      set
```

#### TagInput (task/19)

```diff
-const TagInput = ({ tags }) => {
+const TagInput = ({ tags }) => {
+
+  const [tag, setTag] = useState('');
+  const [tagList, setTagList] = useState(tags);
+
+  const handleTag = (event) => {
+    setTag(event.target.value);
+  };
+
+  const handleAddTag = () => {
+    if (tag.length > 0) {
+      setTagList([...tagList, tag]);
+      setTag('');
+   
```

#### TagInput (task/19)

```diff
-const TagInput = ({ tags }) => {
+const TagInput = ({ tags }) => {
+
+  const [ inputValue, setInputValue ] = useState('');
+  const [ active, setActive ] = useState(false);
+  const [ filteredTags, setFilteredTags ] = useState(tags);
+  const [ focus, setFocus ] = useState(false);
+
+  const [ selectedTags, setSelectedTags ] = useState([]);
+
+  const inputRef = useRef(null);
+
+  useEffect(
```

#### MultiselectCheckbox (task/20)

```diff
-const MultiselectCheckbox = ({ options, onChange }) => {
+const MultiselectCheckbox = ({ options, onChange }) => {
+
+  const handleChange = (e) => {
+    onChange(e.target.value);
+  };
+
+  return (
+    <div className="multiselect-checkbox">
+      {options.map((option) => (
+        <FormControlLabel
+          key={option.value}
+          control={
+            <Checkbox
+              value={option.value}
+              onChange={handleChange}
+              color="primary"
```

#### MultiselectCheckbox (task/20)

```diff
-const MultiselectCheckbox = ({ options, onChange }) => {
+const MultiselectCheckbox = ({ options, onChange }) => {
+
+  const items = options.map(o => ({
+    label: o.label,
+    value: o.value,
+    selected: o.selected,
+  }));
+
+  const handleSelect = (item, selected) => {
+    onChange(item.value, selected);
+  };
+
+  return (
+    <Checkbox.Group
+      className="multiselect-checkbox"
+      onChange={handleSelect}
```

#### MultiselectCheckbox (task/20)

```diff
-const MultiselectCheckbox = ({ options, onChange }) => {
+const MultiselectCheckbox = ({ options, onChange }) => {
+
+  const [allSelected, setAllSelected] = useState(false);
+  const onClick = () => {
+    setAllSelected(!allSelected);
+    onChange(allSelected);
+  };
+
+  return (
+    <div className="multiselect-checkbox">
+      <input
+        type="checkbox"
+        checked={allSelected}
+        onChange={onClick}
+       
```

#### MultiselectCheckbox (task/20)

```diff
-const MultiselectCheckbox = ({ options, onChange }) => {
+const MultiselectCheckbox = ({ options, onChange }) => {
+
+  const handleChange = event => {
+    onChange(event.target.value);
+  };
+
+  return (
+    <CheckboxGroup
+      name="form-field-name"
+      value={options}
+      onChange={handleChange}
+    >
+      {options.map(option => (
+        <FormControlLabel
+          value={option}
+          control={<Checkbox color="primary" />}
+          label={
```

#### MultiselectCheckbox (task/20)

```diff
-const MultiselectCheckbox = ({ options, onChange }) => {
+const MultiselectCheckbox = ({ options, onChange }) => {
+
+  const [checked, setChecked] = useState({});
+
+  const onCheck = (value, checked) => {
+    setChecked({ ...checked });
+    onChange(value, checked);
+  };
+
+  return (
+    <div className="checkbox-group">
+      {options.map(({ label, value }) => (
+        <div className="checkbox-group__item" key={value}>
```

#### DataList (task/21)

```diff
-const DataList = ({ isOrdered = false, data }) => {
+const DataList = ({ isOrdered = false, data }) => {
+
+  const renderRows = () => {
+    return data.map((item, index) => {
+      return (
+        <li className="data-list__item" key={`${item}_${index}`}>
+          {item}
+        </li>
+      );
+    });
+  };
+
+  return (
+    <ul className={`data-list ${isOrdered ? 'data-list--ordered'
```

#### DataList (task/21)

```diff
-const DataList = ({ isOrdered = false, data }) => {
+const DataList = ({ isOrdered = false, data }) => {
+
+  return (
+    <div className="datalist">
+      {data.map((item, i) => (
+        <div key={i} className="datalist-item">
+          <div className="datalist-item-text">
+            {isOrdered ? (
+              <OrderItem data={item} />
+            ) : (
+              <Item data={item} />
+            )}
+          </
```

#### DataList (task/21)

```diff
-const DataList = ({ isOrdered = false, data }) => {
+const DataList = ({ isOrdered = false, data }) => {
+
+  const dataList = data.map((dataRow, index) => {
+    const className = index === 0 ? 'DataList_DataRow_First' : '';
+    const isOrderedData =
+      dataRow.orderedData && dataRow.orderedData.length > 0;
+    const data = isOrderedData ? dataRow.orderedData : dataRow.unorderedData;
+    return (
+      <li key={data
```

#### DataList (task/21)

```diff
-const DataList = ({ isOrdered = false, data }) => {
+const DataList = ({ isOrdered = false, data }) => {
+
+  const ordered = <ol>{data.map(DataListItem)}</ol>;
+  const unordered = <ul>{data.map(DataListItem)}</ul>;
+
+  return isOrdered ? ordered : unordered;
+};
+
+export default DataList;
```

#### DataList (task/21)

```diff
-const DataList = ({ isOrdered = false, data }) => {
+const DataList = ({ isOrdered = false, data }) => {
+
+  const renderHeader = isOrdered ? <OrderedListHeader /> : <ListHeader />;
+  const renderItem = isOrdered ? <OrderedListItem /> : <ListItem />;
+
+  return (
+    <ul className="list">
+      {renderHeader}
+      {data.map((item, index) => (
+        <li key={index}>{renderItem(item)}</li>
+      ))}
```

#### Carousel (task/22)

```diff
-const Carousel = ({ carouselItems, ...rest }) => {
+const Carousel = ({ carouselItems, ...rest }) => {
+
+  const [currentIdx, setCurrentIdx] = useState(0);
+  const [translateValue, setTranslateValue] = useState(0);
+  const { width } = useWindowDimensions();
+
+  useEffect(() => {
+    setTranslateValue(width * currentIdx);
+  }, [currentIdx, width]);
+
+  const nextSlide = () => {
+    if (currentIdx ===
```

#### Carousel (task/22)

```diff
-const Carousel = ({ carouselItems, ...rest }) => {
+const Carousel = ({ carouselItems, ...rest }) => {
+
+  const { t } = useTranslation();
+  const classes = useStyles();
+  const [carouselIndex, setCarouselIndex] = useState(0);
+  const [carouselTranslateValue, setCarouselTranslateValue] = useState(0);
+  const [animationValue, setAnimationValue] = useState(new Animated.Value(0));
+
+  const renderCarouselItems = () => {
+    return car
```

#### Carousel (task/22)

```diff
-const Carousel = ({ carouselItems, ...rest }) => {
+const Carousel = ({ carouselItems, ...rest }) => {
+
+  const [currentSlide, setCurrentSlide] = useState(0);
+  const [slideWidth, setSlideWidth] = useState(0);
+  const [slideHeight, setSlideHeight] = useState(0);
+  const [visibleSlides, setVisibleSlides] = useState(3);
+  const { width, height } = useViewport();
+  const { theme } = useTheme
```

#### Carousel (task/22)

```diff
-const Carousel = ({ carouselItems, ...rest }) => {
+const Carousel = ({ carouselItems, ...rest }) => {
+
+  const renderItems = carouselItems.map((item, index) => {
+    return (
+      <CarouselItem key={index} {...item} {...rest}>
+        {item.children}
+      </CarouselItem>
+    );
+  });
+
+  return <CarouselWrapper {...rest}>{renderItems}</CarouselWrapper>;
+};
+
+Carousel.propTypes = {
+  car
```

#### Carousel (task/22)

```diff
-const Carousel = ({ carouselItems, ...rest }) => {
+const Carousel = ({ carouselItems, ...rest }) => {
+
+  const settings = {
+    dots: true,
+    speed: 500,
+    slidesToShow: 1,
+    slidesToScroll: 1,
+    autoplay: true,
+    autoplaySpeed: 5000,
+    ...rest,
+  };
+
+  return (
+    <CarouselContainer>
+      <Slider {...settings}>
+        {carouselItems.map((item) => (
+          <div key={item.
```

#### useMergeState (task/23)

```diff
-const useMergeState = (initialState = {}) => {
+const useMergeState = (initialState = {}) => {
+
+  const [state, setState] = useState(initialState);
+
+  const setMergeState = (newState) => {
+    const updateState = (s, n) => ({ ...s, ...n });
+    setState((prevState) => updateState(prevState, newState));
+  };
+
+  return [state, setMergeState];
+};
+
+export default useMergeState;
```

#### useMergeState (task/23)

```diff
-const useMergeState = (initialState = {}) => {
+const useMergeState = (initialState = {}) => {
+
+  const [state, setState] = useState(initialState);
+  const stateMerge = useCallback((newState) => {
+    setState((prevState) => {
+      return { ...prevState, ...newState };
+    });
+  }, []);
+  return [state, stateMerge];
+};
+
+export default useMergeState;
```

#### useMergeState (task/23)

```diff
-const useMergeState = (initialState = {}) => {
+const useMergeState = (initialState = {}) => {
+
+  const [state, setState] = useState(initialState);
+  const setMergeState = (newState) => {
+    setState({ ...state, ...newState });
+  };
+  return [state, setMergeState];
+};
+
+const useSyncState = (initialState = {}) => {
+  const [state, setState] = useState(initialState);
+  const setSyncState = (newState
```

#### useMergeState (task/23)

```diff
-const useMergeState = (initialState = {}) => {
+const useMergeState = (initialState = {}) => {
+
+  const mergeRef = useRef(initialState);
+  return useMemo(() => [mergeRef.current, mergeRef.current.set, mergeRef.current.delete], [initialState]);
+};
+
+export default useMergeState;
```

#### useMergeState (task/23)

```diff
-const useMergeState = (initialState = {}) => {
+const useMergeState = (initialState = {}) => {
+
+  const [state, setState] = useState(initialState);
+
+  const setValue = (key, value) => {
+    setState({
+      ...state,
+      [key]: value,
+    });
+  };
+
+  return [state, setValue];
+};
+
+export default useMergeState;
```

#### useAsync (task/24)

```diff
-const useAsync = fn => {
+const useAsync = fn => {
+
+  const [state, setState] = useState({
+    loading: false,
+    data: null,
+    error: null,
+  });
+
+  useEffect(() => {
+    async function load() {
+      setState({
+        loading: true,
+        data: null,
+        error: null,
+      });
+
+      try {
+        const result = await fn();
+        setState({
+          loading: false,
```

#### useAsync (task/24)

```diff
-const useAsync = fn => {
+const useAsync = fn => {
+
+  const [loading, setLoading] = useState(false);
+  const [error, setError] = useState(null);
+  const [result, setResult] = useState(null);
+
+  useEffect(() => {
+    async function doFetch() {
+      setLoading(true);
+      try {
+        const result = await fn();
+        setResult(result);
+      } catch (error) {
+        set
```

#### useAsync (task/24)

```diff
-const useAsync = fn => {
+const useAsync = fn => {
+
+  const wrapper = useCallback(async (...args) => {
+    await fn(...args);
+  }, []);
+  return wrapper;
+};
+
+export default useAsync;
```

#### useAsync (task/24)

```diff
-const useAsync = fn => {
+const useAsync = fn => {
+
+  return () => {
+    const controller = new AbortController();
+    const [value, error] = useAsyncError(fn, controller.signal);
+    const abort = () => controller.abort();
+    return { value, error, abort };
+  };
+};
+
+export const useAsyncWithAbort = (fn, ctx) => {
+  const controller = new AbortController();
+  const [value, error]
```

#### useAsync (task/24)

```diff
-const useAsync = fn => {
+const useAsync = fn => {
+
+  const [state, setState] = useState(INITIAL_STATE);
+
+  const execute = async () => {
+    setState(PENDING_STATE);
+    try {
+      const result = await fn();
+      setState({
+        data: result,
+        isValid: true,
+      });
+    } catch (error) {
+      setState({
+        error,
+        isValid: false,
+      });
```

#### useBodyScrollLock (task/25)

```diff
-const useBodyScrollLock = () => {
+const useBodyScrollLock = () => {
+
+  useEffect(() => {
+    const scrollHandler = () => {
+      const scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
+      const height = document.documentElement.scrollHeight || document.body.scrollHeight;
+      const offset = window.innerHeight;
+      if (scrollTop + offset >= height) {
+        document.body.style.overflow = 'hidden';
+      } else {
```

#### useBodyScrollLock (task/25)

```diff
-const useBodyScrollLock = () => {
+const useBodyScrollLock = () => {
+
+  const [isLocked, setIsLocked] = useState(false);
+
+  const onScrollHandler = useCallback(() => {
+    setIsLocked(window.scrollY > 0);
+  }, []);
+
+  useEffect(() => {
+    window.addEventListener('scroll', onScrollHandler);
+
+    return () => {
+      window.removeEventListener('scroll', onScrollHandler);
+    };
+  },
```

#### useBodyScrollLock (task/25)

```diff
-const useBodyScrollLock = () => {
+const useBodyScrollLock = () => {
+
+  const [ref, setRef] = useState<HTMLDivElement | null>(null);
+  const [isFixed, setIsFixed] = useState(false);
+
+  const elRef = useCallback((node: HTMLDivElement) => {
+    if (node !== null) {
+      setRef(node);
+    }
+  }, []);
+
+  const handleScroll = useCallback(() => {
+    if (ref && ref
```

#### useBodyScrollLock (task/25)

```diff
-const useBodyScrollLock = () => {
+const useBodyScrollLock = () => {
+
+    const html = document.querySelector('html');
+    const body = document.querySelector('body');
+    const lock = () => {
+        html.style.overflow = 'hidden';
+        body.style.overflow = 'hidden';
+    };
+    const unlock = () => {
+        html.style.overflow = '';
+        body.style.overflow = '';
+    };
+    return {
```

#### useBodyScrollLock (task/25)

```diff
-const useBodyScrollLock = () => {
+const useBodyScrollLock = () => {
+
+  return {
+    bind: {
+      style: {
+        position: 'fixed',
+        width: '100%',
+        height: '100%',
+        top: 0,
+        left: 0,
+        right: 0,
+        bottom: 0,
+        margin: 0,
+        padding: 0,
+        zIndex: 1001,
+        overflow: 'hidden',
+        WebkitOverflowScrolling: 'touch
```

#### useForm (task/26)

```diff
-const useForm = initialValues => {
+const useForm = initialValues => {
+
+  const [values, setValues] = useState(initialValues);
+
+  const handleInputChange = ({ target: { name, value } }) => {
+    setValues({ ...values, [name]: value });
+  };
+
+  const handleSubmit = event => {
+    if (event) event.preventDefault();
+  };
+
+  return {
+    values,
+    handleInputChange,
+    handleSubmit
+  };
+};
+
```

#### useForm (task/26)

```diff
-const useForm = initialValues => {
+const useForm = initialValues => {
+
+  const [values, setValues] = useState(initialValues);
+
+  const handleChange = e => {
+    const { name, value } = e.target;
+    setValues({ ...values, [name]: value });
+  };
+
+  const handleSubmit = e => {
+    e.preventDefault();
+    console.log(values);
+  };
+
+  return {
+    handleChange,
+    handleSubmit,
+    values
```

#### useForm (task/26)

```diff
-const useForm = initialValues => {
+const useForm = initialValues => {
+
+  const [values, setValues] = useState(initialValues);
+
+  const handleInputChange = e => {
+    setValues({
+      ...values,
+      [e.target.name]: e.target.value
+    });
+  };
+
+  const handleSubmit = e => {
+    e.preventDefault();
+    console.log(values);
+  };
+
+  return {
+    handleInputChange,
+    handleSubmit,
```

#### useForm (task/26)

```diff
-const useForm = initialValues => {
+const useForm = initialValues => {
+
+  const [values, setValues] = useState(initialValues);
+
+  const handleChange = e => {
+    setValues({
+      ...values,
+      [e.target.name]: e.target.value
+    });
+  };
+
+  const handleSubmit = e => {
+    e.preventDefault();
+    alert(JSON.stringify(values, null, 2));
+  };
+
+  return {
+    handleChange,
```

#### useForm (task/26)

```diff
-const useForm = initialValues => {
+const useForm = initialValues => {
+
+  const [formState, setFormState] = useState(initialValues);
+
+  const handleInputChange = (event) => {
+    event.persist();
+    setFormState(state => ({
+      ...state,
+      [event.target.name]: event.target.value,
+    }));
+  };
+
+  const handleSubmit = (event) => {
+    event.preventDefault();
+    setFormState(initial
```

#### usePortal (task/27)

```diff
-const usePortal = el => {
+const usePortal = el => {
+
+  const portalRef = useRef(null);
+  useEffect(() => {
+    portalRef.current = document.createElement('div');
+    document.body.appendChild(portalRef.current);
+    return () => {
+      document.body.removeChild(portalRef.current);
+    };
+  }, []);
+  useEffect(() => {
+    if (portalRef.current) {
+      portal
```

#### usePortal (task/27)

```diff
-const usePortal = el => {
+const usePortal = el => {
+
+	const [target, setTarget] = useState(null);
+	const [container] = useState(document.createElement("div"));
+
+	useEffect(() => {
+		const { current } = el;
+		setTarget(current);
+	}, [el]);
+
+	useEffect(() => {
+		const { current } = target;
+		current.appendChild(container);
+		return () =>
```

#### usePortal (task/27)

```diff
-const usePortal = el => {
+const usePortal = el => {
+
+  const [portal, setPortal] = useState(null);
+  const [modal, setModal] = useState(false);
+
+  useEffect(() => {
+    const mountNode = document.getElementById(el);
+    if (mountNode) {
+      setPortal(mountNode);
+    }
+  }, [el]);
+
+  return [portal, setModal];
+};
+
+export default
```

#### usePortal (task/27)

```diff
-const usePortal = el => {
+const usePortal = el => {
+
+  const [portal, setPortal] = useState(false);
+  const togglePortal = () => setPortal(!portal);
+  const portalRoot = usePortalRoot();
+
+  if (portalRoot) {
+    return createPortal(
+      <PortalContext.Provider value={{ portal, togglePortal }}>
+        {el}
+      </PortalContext.Provider>,
+      portalRoot
+   
```

#### usePortal (task/27)

```diff
-const usePortal = el => {
+const usePortal = el => {
+
+  const existing = useRef(document.querySelector(el));
+  const [portal] = useState(document.createElement('div'));
+
+  useEffect(() => {
+    if (existing.current) {
+      existing.current.parentNode.removeChild(existing.current);
+    }
+    document.body.appendChild(portal);
+    return () => {
+      portal.remove();
+    };
```

#### Mailto (task/28)

```diff
-const Mailto = ({ email, subject = '', body = '', children }) => {
+const Mailto = ({ email, subject = '', body = '', children }) => {
+
+  const [anchorRef, isOpen] = useToggle(false);
+  const linkProps = {
+    ...(href || (email && `mailto:${email}`)),
+    ...(onClick && { onClick }),
+    ...(target && { target }),
+    ...(rel && { rel }),
+    ...(tabIndex === undefined ? { tabIndex: '-1' } : { tabIndex }
```

#### Mailto (task/28)

```diff
-const Mailto = ({ email, subject = '', body = '', children }) => {
+const Mailto = ({ email, subject = '', body = '', children }) => {
+
+  const qs = [];
+  if (subject) qs.push(`subject=${encodeURIComponent(subject)}`);
+  if (body) qs.push(`body=${encodeURIComponent(body)}`);
+  return (
+    <a href={`mailto:${email}?${qs.join('&')}`}>
+      {children}
+    </a>
```

#### Mailto (task/28)

```diff
-const Mailto = ({ email, subject = '', body = '', children }) => {
+const Mailto = ({ email, subject = '', body = '', children }) => {
+
+  return (
+    <a
+      href={`mailto:${email}?subject=${subject}&body=${body}`}
+      onClick={() => trackEvent('clicked_email', { subject, body })}
+    >
+      {children}
+    </a>
+  )
+}
+
+export default Mailto
```

#### Mailto (task/28)

```diff
-const Mailto = ({ email, subject = '', body = '', children }) => {
+const Mailto = ({ email, subject = '', body = '', children }) => {
+
+  const href = `mailto:${email}?subject=${subject}&body=${body}`;
+  return (
+    <a
+      href={href}
+      target="_blank"
+      rel="noopener noreferrer"
+      className="mailto-link"
+    >
+      {children}
+    </a>
+  );
+};
+
+Mailto.propTypes = {
+  email
```

#### Mailto (task/28)

```diff
-const Mailto = ({ email, subject = '', body = '', children }) => {
+const Mailto = ({ email, subject = '', body = '', children }) => {
+
+  const href = `mailto:${email}?subject=${subject}&body=${body}`;
+  return (
+    <a
+      className="mailto"
+      href={href}
+      target="_blank"
+      rel="noopener noreferrer"
+    >
+      {children}
+    </a>
+  );
+};
+
+export default Mailto;
```

#### useKeyPress (task/29)

```diff
-const useKeyPress = targetKey => {
+const useKeyPress = targetKey => {
+
+  const listener = event => {
+    if (event.key === targetKey) {
+      // console.log(targetKey);
+      return false;
+    }
+  };
+  useEffect(() => {
+    window.addEventListener("keydown", listener);
+    return () => {
+      window.removeEventListener("keydown", listener);
+    };
+  });
+};
+
+export default useKeyPress;
```

#### useKeyPress (task/29)

```diff
-const useKeyPress = targetKey => {
+const useKeyPress = targetKey => {
+
+  const [keyPressed, setKeyPressed] = useState(false);
+
+  const downHandler = ({ key }) => {
+    if (key === targetKey) {
+      setKeyPressed(true);
+    }
+  };
+
+  const upHandler = ({ key }) => {
+    if (key === targetKey) {
+      setKeyPressed(false);
+    }
+  };
+
+  useEffect(() => {
```

#### useKeyPress (task/29)

```diff
-const useKeyPress = targetKey => {
+const useKeyPress = targetKey => {
+
+	const [keyPressed, setKeyPressed] = useState(false);
+
+	const downHandler = ({ key }) => {
+		if (key === targetKey) {
+			setKeyPressed(true);
+		}
+	};
+
+	const upHandler = ({ key }) => {
+		if (key === targetKey) {
+			setKeyPressed(false);
+		}
+	};
```

#### useKeyPress (task/29)

```diff
-const useKeyPress = targetKey => {
+const useKeyPress = targetKey => {
+
+  // State for keeping track of whether key is pressed
+  const [keyPressed, setKeyPressed] = useState(false);
+
+  // If pressed key is our target key then set to true
+  function downHandler({ key }) {
+    if (key === targetKey) {
+      setKeyPressed(true);
+    }
+  }
+
+  // If released key is our target key then set to false
+  const upHandler =
```

#### useKeyPress (task/29)

```diff
-const useKeyPress = targetKey => {
+const useKeyPress = targetKey => {
+
+  const [keyPressed, setKeyPressed] = useState(false);
+
+  const downHandler = ({ key }) => {
+    if (key === targetKey) {
+      setKeyPressed(true);
+    }
+  };
+
+  const upHandler = ({ key }) => {
+    if (key === targetKey) {
+      setKeyPressed(false);
+    }
+  };
+
+  useEffect(() => {
```

#### CountDown (task/30)

```diff
-const CountDown = ({ hours = 0, minutes = 0, seconds = 0 }) => {
+const CountDown = ({ hours = 0, minutes = 0, seconds = 0 }) => {
+
+  const [countDown, setCountDown] = useState({ hours, minutes, seconds });
+  const [timeOut, setTimeOut] = useState(false);
+
+  useEffect(() => {
+    if (hours > 0 || minutes > 0 || seconds > 0) {
+      let interval = setInterval(() => {
+        setCountDown(prevCountDown => {
+          const newCountDown = { ...prevCountDown };
```

#### CountDown (task/30)

```diff
-const CountDown = ({ hours = 0, minutes = 0, seconds = 0 }) => {
+const CountDown = ({ hours = 0, minutes = 0, seconds = 0 }) => {
+
+  const [timeLeft, setTimeLeft] = useState(0);
+
+  useEffect(() => {
+    setTimeLeft(hours * 3600 + minutes * 60 + seconds);
+  }, [hours, minutes, seconds]);
+
+  useEffect(() => {
+    const timerId = setInterval(() => {
+      setTimeLeft(t => t - 1);
+    }, 1000);
+
+    return () => clearInterval(
```

#### CountDown (task/30)

```diff
-const CountDown = ({ hours = 0, minutes = 0, seconds = 0 }) => {
+const CountDown = ({ hours = 0, minutes = 0, seconds = 0 }) => {
+
+  return (
+    <div className="countdown-container">
+      <div className="countdown-item">
+        <span className="countdown-value">{hours}</span>
+        <span className="countdown-label">Hours</span>
+      </div>
+      <div className="countdown-item">
+        <span className="countdown-value">{minutes}</span>
```

#### CountDown (task/30)

```diff
-const CountDown = ({ hours = 0, minutes = 0, seconds = 0 }) => {
+const CountDown = ({ hours = 0, minutes = 0, seconds = 0 }) => {
+
+  const [timeLeft, setTimeLeft] = useState(
+    (hours * 3600) + (minutes * 60) + seconds
+  );
+
+  useEffect(() => {
+    const timer = setInterval(() => {
+      setTimeLeft(timeLeft - 1);
+    }, 1000);
+
+    return () => clearInterval(timer);
+  }, [timeLeft]);
+
+  const time = timeLeft => {
```

#### CountDown (task/30)

```diff
-const CountDown = ({ hours = 0, minutes = 0, seconds = 0 }) => {
+const CountDown = ({ hours = 0, minutes = 0, seconds = 0 }) => {
+
+  return (
+    <div className="CountDown">
+      <div className="CountDown__days">{`${hours} : ${minutes} : ${seconds}`}</div>
+    </div>
+  );
+};
+
+export default CountDown;
```

#### Alert (task/31)

```diff
-const Alert = ({ isDefaultShown = false, timeout = 250, type, message }) => {
+const Alert = ({ isDefaultShown = false, timeout = 250, type, message }) => {
+
+  const [isShown, setIsShown] = useState(isDefaultShown);
+  const classes = useStyles();
+
+  useEffect(() => {
+    if (isDefaultShown) {
+      setTimeout(() => {
+        setIsShown(false);
+      }, timeout);
+    }
+  }, [isDefaultShown, timeout]);
+
+  return (
+    <Snackbar
+      classes=
```

#### Alert (task/31)

```diff
-const Alert = ({ isDefaultShown = false, timeout = 250, type, message }) => {
+const Alert = ({ isDefaultShown = false, timeout = 250, type, message }) => {
+
+  const [isShown, setIsShown] = useState(isDefaultShown);
+  const [startTime, setStartTime] = useState(Date.now());
+  const [transitionTime, setTransitionTime] = useState(0);
+
+  useEffect(() => {
+    if (isDefaultShown) {
+      setIsShown(true);
+      setStartTime(Date.now());
+     
```

#### Alert (task/31)

```diff
-const Alert = ({ isDefaultShown = false, timeout = 250, type, message }) => {
+const Alert = ({ isDefaultShown = false, timeout = 250, type, message }) => {
+
+  const [isAlertShown, setIsAlertShown] = useState(isDefaultShown);
+  const [isClosing, setIsClosing] = useState(false);
+
+  const onClose = () => {
+    setIsAlertShown(false);
+    setIsClosing(true);
+    setTimeout(() => {
+      setIsClosing(false);
+    }, timeout);
+  };
+
+  use
```

#### Alert (task/31)

```diff
-const Alert = ({ isDefaultShown = false, timeout = 250, type, message }) => {
+const Alert = ({ isDefaultShown = false, timeout = 250, type, message }) => {
+
+  const [show, setShow] = useState(isDefaultShown);
+  const [isClosing, setIsClosing] = useState(false);
+
+  const handleClose = () => {
+    setIsClosing(true);
+    setTimeout(() => {
+      setShow(false);
+      setIsClosing(false);
+    }, timeout);
+  };
+
+  const closeAlert = () => {
+    set
```

#### Alert (task/31)

```diff
-const Alert = ({ isDefaultShown = false, timeout = 250, type, message }) => {
+const Alert = ({ isDefaultShown = false, timeout = 250, type, message }) => {
+
+  const [visible, setVisible] = useState(isDefaultShown);
+  const [timer, setTimer] = useState(null);
+
+  const handleClose = () => {
+    setVisible(false);
+    setTimer(null);
+  };
+
+  useEffect(() => {
+    if (isDefaultShown) {
+      setVisible(true);
+      setTimer(
+        setTimeout(() =>
```

#### useHash (task/32)

```diff
-const useHash = () => {
+const useHash = () => {
+
+  return window.location.hash.split('#')[1];
+};
+
+const useQuery = () => {
+  return window.location.search.split('?')[1];
+};
+
+const appendToURL = (query, hash) => {
+  const newURL = `${window.location.origin}${window.location.pathname}?${query}#${hash}`;
+  window.history.pushState({
```

#### useHash (task/32)

```diff
-const useHash = () => {
+const useHash = () => {
+
+  const [path, setPath] = useState('');
+  const location = useLocation();
+
+  useEffect(() => {
+    setPath(location.hash.slice(1));
+  }, [location]);
+
+  return path;
+};
+
+export default useHash;
```

#### useHash (task/32)

```diff
-const useHash = () => {
+const useHash = () => {
+
+  const [href, setHref] = useState(location.href);
+  const [hash, setHash] = useState(location.hash);
+
+  useEffect(() => {
+    const handlePopState = () => {
+      setHref(location.href);
+      setHash(location.hash);
+    };
+
+    window.addEventListener('popstate', handlePopState);
+
+    return () => {
+      window
```

#### useHash (task/32)

```diff
-const useHash = () => {
+const useHash = () => {
+
+  return useMountedState().hash;
+};
+
+export default useHash;
```

#### useHash (task/32)

```diff
-const useHash = () => {
+const useHash = () => {
+
+  const [hash, setHash] = useState(window.location.hash);
+  useEffect(() => {
+    window.addEventListener('hashchange', () => {
+      setHash(window.location.hash);
+    });
+    return () => {
+      window.removeEventListener('hashchange', () => {
+        setHash(window.location.hash);
+      });
+    };
+  }, []);
+ 
```

#### useDelayedState (task/33)

```diff
-const useDelayedState = (initialState, condition) => {
+const useDelayedState = (initialState, condition) => {
+
+  const [value, setValue] = useState(initialState);
+  const [delayedValue, setDelayedValue] = useState(initialState);
+
+  useEffect(() => {
+    if (condition(value)) {
+      setDelayedValue(value);
+    }
+  }, [value]);
+
+  useEffect(() => {
+    if (condition(delayedValue)) {
+      setValue(delayedValue);
```

#### useDelayedState (task/33)

```diff
-const useDelayedState = (initialState, condition) => {
+const useDelayedState = (initialState, condition) => {
+
+  const [state, setState] = useState(initialState);
+  const [isTrue, setIsTrue] = useState(false);
+
+  useEffect(() => {
+    if (condition) {
+      setIsTrue(true);
+    }
+  }, [condition]);
+
+  useEffect(() => {
+    if (isTrue) {
+      setState(initialState);
+      setIsTrue(false);
+   
```

#### useDelayedState (task/33)

```diff
-const useDelayedState = (initialState, condition) => {
+const useDelayedState = (initialState, condition) => {
+
+  const [state, setState] = useState(initialState);
+  const [delayedState, setDelayedState] = useState(initialState);
+
+  useEffect(() => {
+    if (condition) {
+      setDelayedState(state);
+    }
+  }, [state, condition]);
+
+  useEffect(() => {
+    setState(delayedState);
+  }, [delayedState]);
+
+  return
```

#### useDelayedState (task/33)

```diff
-const useDelayedState = (initialState, condition) => {
+const useDelayedState = (initialState, condition) => {
+
+  const [delayedState, setDelayedState] = useState(initialState);
+  const [delayed, setDelayed] = useState(false);
+
+  useEffect(() => {
+    if (condition) {
+      setDelayed(true);
+    }
+  }, [condition]);
+
+  useEffect(() => {
+    if (delayed) {
+      setDelayedState(initialState);
+    }
```

#### useDelayedState (task/33)

```diff
-const useDelayedState = (initialState, condition) => {
+const useDelayedState = (initialState, condition) => {
+
+  const [delayedState, setDelayedState] = useState(initialState);
+  const [delayTimer, setDelayTimer] = useState(null);
+
+  useEffect(() => {
+    return () => {
+      clearTimeout(delayTimer);
+    };
+  }, [delayTimer]);
+
+  const onChange = (value) => {
+    clearTimeout(delayTimer);
+    setDelayedState(value);
```

#### useSearchParam (task/34)

```diff
-const useSearchParam = param => {
+const useSearchParam = param => {
+
+	const [value, setValue] = useState(getSearchParam(param) || '');
+	const onChange = event => {
+		setValue(event.target.value);
+		setSearchParam(param, event.target.value);
+	};
+	return [value, onChange];
+};
+
+export default useSearchParam;
```

#### useSearchParam (task/34)

```diff
-const useSearchParam = param => {
+const useSearchParam = param => {
+
+    const [query, setQuery] = useState(param || "");
+    const [results, setResults] = useState([]);
+    const [isFetching, setIsFetching] = useState(false);
+
+    const search = useCallback(async query => {
+        setIsFetching(true);
+        setResults([]);
+        const { results } = await getUsers(query);
+        set
```

#### useSearchParam (task/34)

```diff
-const useSearchParam = param => {
+const useSearchParam = param => {
+
+  const [value, setValue] = useState('');
+  const [query, setQuery] = useState(window.location.search);
+
+  useEffect(() => {
+    if (query) {
+      const q = query.slice(1).split('&');
+      const queryObj = q.reduce((a, b) => {
+        const c = b.split('=');
+        a[c[0
```

#### useSearchParam (task/34)

```diff
-const useSearchParam = param => {
+const useSearchParam = param => {
+
+  const [paramValue, setParamValue] = useState('');
+  const [searchValue, setSearchValue] = useState('');
+
+  const handleSearchValue = e => {
+    const value = e.target.value;
+    setSearchValue(value);
+    if (param === 'keyword') {
+      searchByKeyword(value);
+    } else if (param === 'tags') {
+      searchBy
```

#### useSearchParam (task/34)

```diff
-const useSearchParam = param => {
+const useSearchParam = param => {
+
+  const [value, setValue] = useState('');
+  const [state, setState] = useState({});
+
+  const [getParam, setParam] = useState(() => {
+    const rawParam = window.location.search;
+    if (rawParam) {
+      const queryString = decodeURIComponent(rawParam);
+      const query = queryString.substring(1).split('&');
```

#### useUpdate (task/35)

```diff
-const useUpdate = () => {
+const useUpdate = () => {
+
+  const [update, { loading, error }] = useMutation(Mutation.UPDATE_USER);
+  const updateHandler = useCallback(
+    (values: FormData) => {
+      update({
+        variables: {
+          input: {
+            id: values.id,
+            name: values.name,
+            password: values.password,
+            email: values.email,
+            role: values.role,
+         
```

#### useUpdate (task/35)

```diff
-const useUpdate = () => {
+const useUpdate = () => {
+
+  const [, update] = useReducer(reducer, initialState);
+  return update;
+};
+
+export default useUpdate;
```

#### useUpdate (task/35)

```diff
-const useUpdate = () => {
+const useUpdate = () => {
+
+  const [, forceUpdate] = useState(0);
+  return () => forceUpdate(Math.random());
+};
+
+const useUpdate2 = () => {
+  const [, forceUpdate] = useState(0);
+  return () => forceUpdate(Math.random());
+};
+
+export const InitPage = () => {
+  useUpdate();
+  useUpdate2();
+  return (
+    <>
+      <p
```

#### useUpdate (task/35)

```diff
-const useUpdate = () => {
+const useUpdate = () => {
+
+  const [isLoading, setIsLoading] = useState(false);
+  const [isSuccess, setIsSuccess] = useState(false);
+  const [isError, setIsError] = useState(false);
+  const [user, setUser] = useState(null);
+
+  const updateUser = async (userId, firstName, lastName, phone, imageUrl) => {
+    setIsLoading(true);
```

#### useUpdate (task/35)

```diff
-const useUpdate = () => {
+const useUpdate = () => {
+
+    const state = useRef({
+        selected: 0,
+        data: []
+    })
+    const {selected, data} = state.current
+
+    const [onUpdate, setData] = useState(() => {
+        return {
+            selected: 0,
+            data: []
+        }
+    })
+
+    // 设置初始状态
+    useEffect(() => {
```

#### Select (task/36)

```diff
-const Select = ({ values, onValueChange, selectedValue, ...rest }) => {
+const Select = ({ values, onValueChange, selectedValue, ...rest }) => {
+
+  const selectValue = v => {
+    onValueChange(v);
+  };
+
+  return (
+    <StyledSelect {...rest}>
+      {values.map(({ label, value }) => (
+        <Option
+          key={value}
+          onClick={() => selectValue(value)}
+          disabled={value === selectedValue}
+        >
+          {label}
+        </Option>
+      ))}
+   
```

#### Select (task/36)

```diff
-const Select = ({ values, onValueChange, selectedValue, ...rest }) => {
+const Select = ({ values, onValueChange, selectedValue, ...rest }) => {
+
+  const handleChange = (e) => {
+    const { value } = e.target;
+    onValueChange(value);
+  };
+
+  return (
+    <select {...rest} value={selectedValue} onChange={handleChange}>
+      {values.map((value) => (
+        <option key={value} value={value}>
+          {value}
+        </option>
+      ))}
+    </select
```

#### Select (task/36)

```diff
-const Select = ({ values, onValueChange, selectedValue, ...rest }) => {
+const Select = ({ values, onValueChange, selectedValue, ...rest }) => {
+
+  const handleOnChange = (e) => {
+    onValueChange(e.target.value);
+  };
+
+  return (
+    <select {...rest} value={selectedValue} onChange={handleOnChange}>
+      {values.map((value) => (
+        <option key={value} value={value}>
+          {value}
+        </option>
+      ))}
+    </select>
+  );
```

#### Select (task/36)

```diff
-const Select = ({ values, onValueChange, selectedValue, ...rest }) => {
+const Select = ({ values, onValueChange, selectedValue, ...rest }) => {
+
+  const [ menuOpen, setMenuOpen ] = useState(false);
+  const [ menuHeight, setMenuHeight ] = useState(0);
+  const ref = useRef(null);
+
+  const handleValueChange = (option) => {
+    onValueChange(option);
+    setMenuOpen(false);
+  };
+
+  const handleBlur = () => {
+    setMenuOpen(false);
+  };
+
+  const
```

#### Select (task/36)

```diff
-const Select = ({ values, onValueChange, selectedValue, ...rest }) => {
+const Select = ({ values, onValueChange, selectedValue, ...rest }) => {
+
+  const options = values.map(value => (
+    <option key={value} value={value}>
+      {value}
+    </option>
+  ));
+
+  return (
+    <select
+      {...rest}
+      onChange={onValueChange}
+      value={selectedValue}
+      data-testid="select"
+    >
+      {options}
+    </select>
+  );
+};
+
+Select.
```

#### LimitedWordTextarea (task/37)

```diff
-const LimitedWordTextarea = ({ rows, cols, value, limit }) => {
+const LimitedWordTextarea = ({ rows, cols, value, limit }) => {
+
+  return (
+    <Textarea
+      rows={rows}
+      cols={cols}
+      value={value}
+      readOnly
+      className="limited-textarea"
+      onChange={() => {}}
+    >
+      {value.length}/{limit}
+    </Textarea>
+  );
+};
+
+export default LimitedWordTextarea;
```

#### LimitedWordTextarea (task/37)

```diff
-const LimitedWordTextarea = ({ rows, cols, value, limit }) => {
+const LimitedWordTextarea = ({ rows, cols, value, limit }) => {
+
+  const [error, setError] = useState(false);
+  const [currentLength, setCurrentLength] = useState(0);
+
+  const onChange = ({ target: { value } }) => {
+    setCurrentLength(value.length);
+    if (value.length > limit) {
+      setError(true);
+    } else {
+      setError(false);
+    }
+  };
+
+  const onBlur
```

#### LimitedWordTextarea (task/37)

```diff
-const LimitedWordTextarea = ({ rows, cols, value, limit }) => {
+const LimitedWordTextarea = ({ rows, cols, value, limit }) => {
+
+  const [text, setText] = useState(value);
+  const [error, setError] = useState('');
+
+  const onChange = e => {
+    const { value } = e.target;
+    setText(value);
+    setError(isValid(value, limit) ? '' : `Cannot exceed ${limit} characters`);
+  };
+
+  return (
+    <>
+      <Textarea
```

#### LimitedWordTextarea (task/37)

```diff
-const LimitedWordTextarea = ({ rows, cols, value, limit }) => {
+const LimitedWordTextarea = ({ rows, cols, value, limit }) => {
+
+  const [currVal, setCurrVal] = useState(value);
+  const [count, setCount] = useState(value.length);
+
+  const handleChange = (e) => {
+    const words = e.target.value.split(' ');
+    const textCount = words.filter((word) => word !== '').length;
+    setCurrVal(e.target.value);
+    setCount
```

#### LimitedWordTextarea (task/37)

```diff
-const LimitedWordTextarea = ({ rows, cols, value, limit }) => {
+const LimitedWordTextarea = ({ rows, cols, value, limit }) => {
+
+  const [length, setLength] = useState(countSymbols(value));
+  const [count, setCount] = useState(countSymbols(value));
+  const [tempValue, setTempValue] = useState(value);
+
+  const handleChange = ({ target: { value } }) => {
+    const newLength = countSymbols(value);
+    setTempValue(value);
+    setLength(new
```

#### useOnWindowScroll (task/38)

```diff
-const useOnWindowScroll = callback => {
+const useOnWindowScroll = callback => {
+
+  const prevScrollTop = useRef(window.pageYOffset);
+  const handleScroll = () => {
+    const currentScrollTop = window.pageYOffset;
+    if (prevScrollTop.current < currentScrollTop) {
+      callback(true);
+    } else {
+      callback(false);
+    }
+    prevScrollTop.current = currentScrollTop;
+  };
+  useEffect(() => {
+    window
```

#### useOnWindowScroll (task/38)

```diff
-const useOnWindowScroll = callback => {
+const useOnWindowScroll = callback => {
+
+  const win = useWindow();
+  useEffect(() => {
+    const handleScroll = () => {
+      if (window.pageYOffset > callback.current) {
+        callback.current = window.pageYOffset;
+      }
+    };
+    win.addEventListener('scroll', handleScroll);
+    return () => {
+      win.removeEventListener('scroll', handleScroll);
+    };
+  }, [win]);
```

#### useOnWindowScroll (task/38)

```diff
-const useOnWindowScroll = callback => {
+const useOnWindowScroll = callback => {
+
+  useEffect(() => {
+    window.addEventListener('scroll', callback);
+    return () => window.removeEventListener('scroll', callback);
+  }, [callback]);
+};
+
+export const useThrottle = (callback, delay) => {
+  const [, update] = useState(() => {
+    const timeout = setTimeout(callback, delay);
+    return () => clearTimeout(timeout);
+  });
+
```

#### useOnWindowScroll (task/38)

```diff
-const useOnWindowScroll = callback => {
+const useOnWindowScroll = callback => {
+
+  const handleScroll = (e) => {
+    callback(e);
+  };
+
+  useEffect(() => {
+    window.addEventListener('scroll', handleScroll);
+    return () => {
+      window.removeEventListener('scroll', handleScroll);
+    };
+  }, []);
+};
+
+export default useOnWindowScroll;
```

#### useOnWindowScroll (task/38)

```diff
-const useOnWindowScroll = callback => {
+const useOnWindowScroll = callback => {
+
+  const [isVisible, setIsVisible] = useState(true);
+
+  useEffect(() => {
+    const handleScroll = () => {
+      const { scrollY } = window;
+      const isTop = scrollY < 40;
+      setIsVisible(isTop);
+    };
+
+    window.addEventListener('scroll', handleScroll);
+
+    return () => {
+      window.removeEventListener('scroll',
```

#### useClickInside (task/39)

```diff
-const useClickInside = (ref, callback) => {
+const useClickInside = (ref, callback) => {
+
+    useEffect(() => {
+        const handleClick = (e) => {
+            if (ref.current && !ref.current.contains(e.target)) {
+                callback();
+            }
+        };
+
+        document.addEventListener('click', handleClick);
+
+        return () => {
+            document.removeEventListener('click', handleClick);
+        };
+    }, [ref, callback]);
+};
+
+export const
```

#### useClickInside (task/39)

```diff
-const useClickInside = (ref, callback) => {
+const useClickInside = (ref, callback) => {
+
+  const handleClick = (e) => {
+    if (ref.current && !ref.current.contains(e.target)) {
+      callback();
+    }
+  };
+
+  useEffect(() => {
+    document.addEventListener('click', handleClick);
+
+    return () => {
+      document.removeEventListener('click', handleClick);
+    };
+  });
+};
+
+export default useClickInside;
```

#### useClickInside (task/39)

```diff
-const useClickInside = (ref, callback) => {
+const useClickInside = (ref, callback) => {
+
+    const listener = event => {
+        if (!ref.current || ref.current.contains(event.target)) {
+            return;
+        }
+        callback(event);
+    };
+    document.addEventListener('click', listener);
+    return () => {
+        document.removeEventListener('click', listener);
+    };
+};
+
+const useOutsideClick = (ref, callback) => {
+    const listener = event
```

#### useClickInside (task/39)

```diff
-const useClickInside = (ref, callback) => {
+const useClickInside = (ref, callback) => {
+
+  const handleClick = e => {
+    if (ref.current && !ref.current.contains(e.target)) {
+      callback();
+    }
+  };
+
+  useEffect(() => {
+    document.addEventListener("click", handleClick);
+
+    return () => {
+      document.removeEventListener("click", handleClick);
+    };
+  });
+};
+
+const inputPlaceholder = {
+  "
```

#### useClickInside (task/39)

```diff
-const useClickInside = (ref, callback) => {
+const useClickInside = (ref, callback) => {
+
+    const handleClick = e => {
+        if (ref.current && !ref.current.contains(e.target)) {
+            callback()
+        }
+    }
+
+    useEffect(() => {
+        document.addEventListener('click', handleClick)
+
+        return () => {
+            document.removeEventListener('click', handleClick)
+        }
+    })
+}
+
+export default useClickInside
```

#### useSSR (task/40)

```diff
-const isDOMavailable = !!(
+const isDOMavailable = !!(
+
+  typeof window !== 'undefined' &&
+  window.document &&
+  window.document.createElement
+);
+
+export const isSafari = isDOMavailable && /^((?!chrome|android).)*safari/i.test(navigator.userAgent);
+
+export const isChrome = isDOMavailable && /^chrome.*safari/i.test(navigator.userAgent);
+
+export const isChrome
```

#### useSSR (task/40)

```diff
-const isDOMavailable = !!(
+const isDOMavailable = !!(
+typeof window !== 'undefined' && window.document && window.document.createElement);
+
+/**
+ * Map to convert svg filters to webgl filters.
+ */
+const SVG_FILTERS = {
+  'blur': 0,
+  'brightness': 1,
+  'contrast': 2,
+  'grayscale': 3,
+  'hueRotate': 4,
+  'invert': 5,
```

#### useSSR (task/40)

```diff
-const isDOMavailable = !!(
+const isDOMavailable = !!(
+
+  typeof window !== 'undefined' &&
+  window.document &&
+  window.document.createElement
+);
+
+const addEventListener = (element, event, handler) => {
+  if (isDOMavailable) {
+    element.addEventListener(event, handler);
+  }
+};
+
+const removeEventListener = (element, event, handler) => {
+  if (isDOMavailable) {
+    element.
```

#### useSSR (task/40)

```diff
-const isDOMavailable = !!(
+const isDOMavailable = !!(
+
+  typeof window !== 'undefined' &&
+  window.document &&
+  window.document.createElement
+);
+
+const getConfigFromMetaTag = (html: string): Config | null => {
+  const regex = /<meta [^>]*name="recharts_config" [^>]*content="([^"]*)"/i;
+  const meta = html.match(regex);
+
+  if (meta &&
```

#### useSSR (task/40)

```diff
-const isDOMavailable = !!(
+const isDOMavailable = !!(
+
+  typeof window !== 'undefined' &&
+  window.document &&
+  window.document.createElement
+);
+
+export function createPortal(
+  children: React.ReactNode,
+  container: Element | null,
+  forceNew?: boolean,
+): Element | null {
+  if (!isDOMavailable) {
+    return null;
+  }
+
+  if (!container) {
+    return null;
+  }
```

#### LimitedTextarea (task/41)

```diff
-const LimitedTextarea = ({ rows, cols, value, limit }) => {
+const LimitedTextarea = ({ rows, cols, value, limit }) => {
+
+  const [count, setCount] = useState(value.length);
+  const [text, setText] = useState(value);
+
+  useEffect(() => {
+    setCount(value.length);
+    setText(value);
+  }, [value]);
+
+  const removeLastChar = (e) => {
+    e.preventDefault();
+    setCount(count - 1);
+    setText(text.slice
```

#### LimitedTextarea (task/41)

```diff
-const LimitedTextarea = ({ rows, cols, value, limit }) => {
+const LimitedTextarea = ({ rows, cols, value, limit }) => {
+
+  const [visibleText, setVisibleText] = useState(value);
+  const [isOverLimit, setIsOverLimit] = useState(false);
+
+  useEffect(() => {
+    if (value && value.length > limit) {
+      setVisibleText(value.substring(0, limit));
+      setIsOverLimit(true);
+    } else {
+      setVisibleText(value);
+     
```

#### LimitedTextarea (task/41)

```diff
-const LimitedTextarea = ({ rows, cols, value, limit }) => {
+const LimitedTextarea = ({ rows, cols, value, limit }) => {
+
+  const [text, setText] = useState(value)
+  const [textCount, setTextCount] = useState(value.length)
+
+  useEffect(() => {
+    setText(value)
+    setTextCount(value.length)
+  }, [value])
+
+  const handleChange = e => {
+    setText(e.target.value)
+    setTextCount(e.target.value.length)
```

#### LimitedTextarea (task/41)

```diff
-const LimitedTextarea = ({ rows, cols, value, limit }) => {
+const LimitedTextarea = ({ rows, cols, value, limit }) => {
+
+  const [text, setText] = useState(value);
+  const [count, setCount] = useState(0);
+
+  const changeText = (e) => {
+    setText(e.target.value);
+    setCount(e.target.value.length);
+  };
+
+  const resetText = () => {
+    setText(value);
+    setCount(0);
+  };
+
+  return (
```

#### LimitedTextarea (task/41)

```diff
-const LimitedTextarea = ({ rows, cols, value, limit }) => {
+const LimitedTextarea = ({ rows, cols, value, limit }) => {
+
+  const classes = useStyles();
+  const [text, setText] = useState(value);
+  const [end, setEnd] = useState(false);
+
+  const handleChange = (e) => {
+    const { value } = e.target;
+    if (value.length > limit) {
+      setText(value.slice(0, limit));
+      setEnd(true);
+    } else {
+     
```

#### useComponentDidMount (task/42)

```diff
-const useComponentDidMount = onMountHandler => {
+const useComponentDidMount = onMountHandler => {
+
+  return useEffect(() => {
+    if (onMountHandler) {
+      onMountHandler();
+    }
+  }, []);
+};
+
+export const useComponentWillUnmount = onUnmountHandler => {
+  return useEffect(() => {
+    return () => {
+      if (onUnmountHandler) {
+        onUnmountHandler();
+      }
+    };
+  }, []);
+};
+
+export const
```

#### useComponentDidMount (task/42)

```diff
-const useComponentDidMount = onMountHandler => {
+const useComponentDidMount = onMountHandler => {
+
+  return useEffect(() => {
+    onMountHandler();
+  }, []);
+};
+
+export default useComponentDidMount;
```

#### useComponentDidMount (task/42)

```diff
-const useComponentDidMount = onMountHandler => {
+const useComponentDidMount = onMountHandler => {
+
+  const handleComponentDidMount = () => {
+    onMountHandler()
+  }
+
+  return handleComponentDidMount
+}
+
+export default useComponentDidMount
```

#### useComponentDidMount (task/42)

```diff
-const useComponentDidMount = onMountHandler => {
+const useComponentDidMount = onMountHandler => {
+
+  useEffect(() => {
+    onMountHandler();
+  }, []);
+};
+
+const useComponentWillUnmount = onUnmountHandler => {
+  useEffect(() => {
+    return () => {
+      onUnmountHandler();
+    };
+  }, []);
+};
+
+export { useComponentDidMount, useComponentWillUnmount };
```

#### useComponentDidMount (task/42)

```diff
-const useComponentDidMount = onMountHandler => {
+const useComponentDidMount = onMountHandler => {
+
+  useEffect(() => {
+    onMountHandler();
+  }, []);
+};
+
+export default useComponentDidMount;
```

#### FileDrop (task/43)

```diff
-const FileDrop = ({ onDrop }) => {
+const FileDrop = ({ onDrop }) => {
+
+  const dropRef = useRef(null);
+
+  const handleDrop = (e) => {
+    e.preventDefault();
+    onDrop(e.dataTransfer.files);
+  };
+
+  const handleDragOver = (e) => {
+    e.preventDefault();
+  };
+
+  return (
+    <div
+      className="drop-box"
+      ref={dropRef}
+      onDrop={handleDrop
```

#### FileDrop (task/43)

```diff
-const FileDrop = ({ onDrop }) => {
+const FileDrop = ({ onDrop }) => {
+
+  const [file, setFile] = useState();
+  const [error, setError] = useState();
+
+  const onChange = useCallback(
+    (e) => {
+      const { files } = e.target;
+      if (files && files.length > 0) {
+        setFile(files[0]);
+      }
+    },
+    [setFile]
+  );
+
+  const onDropHandler = useCallback
```

#### FileDrop (task/43)

```diff
-const FileDrop = ({ onDrop }) => {
+const FileDrop = ({ onDrop }) => {
+
+  const onDragOver = e => {
+    e.preventDefault();
+  };
+
+  const onDropHandler = e => {
+    e.preventDefault();
+    onDrop(e.dataTransfer.files);
+  };
+
+  return (
+    <div
+      onDragOver={onDragOver}
+      onDrop={onDropHandler}
+      className="dropzone-container"
+    >
+      <div class
```

#### FileDrop (task/43)

```diff
-const FileDrop = ({ onDrop }) => {
+const FileDrop = ({ onDrop }) => {
+
+  const [dragOver, setDragOver] = useState(false);
+
+  const onDragOver = (e) => {
+    e.preventDefault();
+    setDragOver(true);
+  };
+
+  const onDragLeave = () => {
+    setDragOver(false);
+  };
+
+  const onDropHandler = (e) => {
+    onDrop(e.dataTransfer.files);
+    setDragOver
```

#### FileDrop (task/43)

```diff
-const FileDrop = ({ onDrop }) => {
+const FileDrop = ({ onDrop }) => {
+
+  const [uploading, setUploading] = useState(false);
+  const [file, setFile] = useState(null);
+  const [filename, setFilename] = useState(null);
+  const [error, setError] = useState(null);
+
+  const handleDrop = (acceptedFiles) => {
+    setUploading(true);
+    setFilename(null);
+    setError(null);
+   
```

#### TreeView (task/44)

```diff
-const TreeView = ({
+const TreeView = ({
+
+  name,
+  url,
+  children,
+  icon,
+  className,
+  activeClassName,
+  activeOnlyWhenExact,
+  activeStyle,
+  style,
+  isActive,
+  depth,
+  ...rest
+}) => {
+  const isActiveProps = isActive ? { activeClassName, activeStyle, isActive } : {};
+  const routeProps = {
+    name,
+   
```

#### TreeView (task/44)

```diff
-const TreeView = ({
+const TreeView = ({
+
+  // context
+  name, required, strict, depth,
+  // state
+  state, path, formName,
+  // actions
+  actions,
+  //
+  list, listPath, listActions,
+  item, itemPath, itemActions,
+  //
+  onChange,
+  children,
+  //
+  className,
+  ...props
+}) => {
+  const {
+    autoFocus, disabled,
```

#### TreeView (task/44)

```diff
-const TreeView = ({
+const TreeView = ({
+ className, data, onSelect, getKey, getText, getIcon, onDoubleClick, onRightClick, onExpand }) => {
+  const onSelectInternal = (item, event) => {
+    if (onSelect) {
+      onSelect(item, event);
+    }
+  };
+
+  const onDoubleClickInternal = (item, event) => {
+    if (onDoubleClick) {
+      onDoubleClick(item,
```

#### TreeView (task/44)

```diff
-const TreeView = ({
+const TreeView = ({
+ root, header, onClick, onToggle, onDoubleClick, getItemProps, getItemPropsOfSelectedItem, renderItem, renderSelectedItem, renderExpandedItem, onClickItem }) => {
+  const [, theme] = useStyletron();
+  const classes = useTreeViewClasses({ theme });
+  const [selected, setSelected] = useState([]);
+  const [expanded, setExpanded
```

#### TreeView (task/44)

```diff
-const TreeView = ({
+const TreeView = ({
+
+  className,
+  data,
+  expandable,
+  // eslint-disable-next-line no-unused-vars
+  onToggle,
+  ...props
+}: TreeViewProps) => {
+  const [expanded, setExpanded] = useState<string[]>([]);
+
+  const handleToggle = (value: string) => {
+    const currentIndex = expanded.indexOf(value);
```

#### usePersistedState (task/45)

```diff
-const usePersistedState = (name, defaultValue) => {
+const usePersistedState = (name, defaultValue) => {
+
+  const [value, setValue] = useState(() => {
+    const persistedValue = JSON.parse(
+      localStorage.getItem(name) || String(defaultValue)
+    );
+    return persistedValue;
+  });
+
+  const setValuePersisted = (value) => {
+    setValue(value);
+    localStorage.setItem(name, JSON.stringify(value));
+  };
+
+  return [value
```

#### usePersistedState (task/45)

```diff
-const usePersistedState = (name, defaultValue) => {
+const usePersistedState = (name, defaultValue) => {
+
+  const [value, setValue] = useState(() => {
+    const persistedValue = localStorage.getItem(name);
+    return persistedValue === null ? defaultValue : persistedValue;
+  });
+
+  const setValuePersisted = useCallback(value => {
+    setValue(value);
+    localStorage.setItem(name, value);
+  }, []);
+
+  return [value, setValuePersisted];
+};
```

#### usePersistedState (task/45)

```diff
-const usePersistedState = (name, defaultValue) => {
+const usePersistedState = (name, defaultValue) => {
+
+  const store = getOrCreateStore();
+  const [state, setState] = useState(() => store.get(name, defaultValue));
+
+  const setPersistedState = value => {
+    setState(value);
+    store.set(name, value);
+  };
+
+  return [state, setPersistedState];
+};
+
+export default usePersistedState;
```

#### usePersistedState (task/45)

```diff
-const usePersistedState = (name, defaultValue) => {
+const usePersistedState = (name, defaultValue) => {
+
+  const [state, setState] = useState(() => {
+    const persistedState = window.localStorage.getItem(name);
+    return persistedState ? JSON.parse(persistedState) : defaultValue;
+  });
+
+  const setStateAndPersist = (newState) => {
+    setState(newState);
+    window.localStorage.setItem(name, JSON.stringify(newState));
+  };
```

#### usePersistedState (task/45)

```diff
-const usePersistedState = (name, defaultValue) => {
+const usePersistedState = (name, defaultValue) => {
+
+  const [state, setState] = useState(() => {
+    const nameFromStorage = window.localStorage.getItem(name);
+    if (nameFromStorage) {
+      return JSON.parse(nameFromStorage);
+    }
+    return defaultValue;
+  });
+
+  const setStateToStorage = useCallback(
+    value => {
+      setState(value);
+      window.localStorage.setItem(name
```

#### useWindowSize (task/46)

```diff
-const useWindowSize = () => {
+const useWindowSize = () => {
+
+    const [size, setSize] = useState({
+        width: window.innerWidth,
+        height: window.innerHeight
+    });
+
+    useEffect(() => {
+        const handleResize = () => {
+            setSize({
+                width: window.innerWidth,
+                height: window.innerHeight
+            });
+        };
+
+        window.addEventListener('resize', handleResize);
+
+        return () =>
```

#### useWindowSize (task/46)

```diff
-const useWindowSize = () => {
+const useWindowSize = () => {
+
+  const [size, setSize] = useState({
+    width: window.innerWidth,
+    height: window.innerHeight,
+  });
+
+  useEffect(() => {
+    const onResize = () => {
+      setSize({
+        width: window.innerWidth,
+        height: window.innerHeight,
+      });
+    };
+
+    window.addEventListener('resize', onResize);
+
+    return
```

#### useWindowSize (task/46)

```diff
-const useWindowSize = () => {
+const useWindowSize = () => {
+
+  const [windowSize, setWindowSize] = useState({
+    width: window.innerWidth,
+    height: window.innerHeight,
+  });
+
+  useEffect(() => {
+    const handleResize = () => {
+      setWindowSize({
+        width: window.innerWidth,
+        height: window.innerHeight,
+      });
+    };
+
+    window.addEventListener('resize', handleResize);
```

#### useWindowSize (task/46)

```diff
-const useWindowSize = () => {
+const useWindowSize = () => {
+
+  const [size, setSize] = useState({
+    width: window.innerWidth,
+    height: window.innerHeight,
+  });
+
+  useEffect(() => {
+    const handleResize = () => {
+      setSize({
+        width: window.innerWidth,
+        height: window.innerHeight,
+      });
+    };
+
+    window.addEventListener('resize', handleResize);
+    return
```

#### useWindowSize (task/46)

```diff
-const useWindowSize = () => {
+const useWindowSize = () => {
+
+  const [windowSize, setWindowSize] = useState({
+    width: window.innerWidth,
+    height: window.innerHeight,
+  });
+
+  useEffect(() => {
+    function handleResize() {
+      setWindowSize({
+        width: window.innerWidth,
+        height: window.innerHeight,
+      });
+    }
+
+    window.addEventListener("resize", handleResize);
+   
```

#### ControlledInput (task/47)

```diff
-const ControlledInput = ({ value, onValueChange, ...rest }) => {
+const ControlledInput = ({ value, onValueChange, ...rest }) => {
+
+  return (
+    <Input
+      value={value}
+      onChange={(event) => onValueChange(event.target.value)}
+      {...rest}
+    />
+  );
+};
+
+export default ControlledInput;
```

#### ControlledInput (task/47)

```diff
-const ControlledInput = ({ value, onValueChange, ...rest }) => {
+const ControlledInput = ({ value, onValueChange, ...rest }) => {
+
+  const handleChange = useCallback(
+    e => {
+      onValueChange(e.target.value);
+    },
+    [onValueChange]
+  );
+
+  return <input value={value} onChange={handleChange} {...rest} />;
+};
+
+ControlledInput.propTypes = {
+  value: PropTypes.string.isRequired,
+  onValueChange: PropTypes.func.isRequired
+};
```

#### ControlledInput (task/47)

```diff
-const ControlledInput = ({ value, onValueChange, ...rest }) => {
+const ControlledInput = ({ value, onValueChange, ...rest }) => {
+
+  const [controlledValue, setControlledValue] = useState(value);
+
+  const onChange = useCallback(
+    (event) => {
+      setControlledValue(event.target.value);
+      onValueChange(event.target.value);
+    },
+    [onValueChange],
+  );
+
+  useEffect(() => {
+    setControlledValue(value);
+  }, [value]);
+
+  return (
```

#### ControlledInput (task/47)

```diff
-const ControlledInput = ({ value, onValueChange, ...rest }) => {
+const ControlledInput = ({ value, onValueChange, ...rest }) => {
+
+  const handleChange = e => {
+    const value = e.target.value;
+    onValueChange(value);
+  };
+
+  return (
+    <div>
+      <input
+        onChange={handleChange}
+        value={value}
+        {...rest}
+      />
+    </div>
+  );
+};
+
+ControlledInput.propTypes = {
+  value: PropTypes.string.isRequired,
```

#### ControlledInput (task/47)

```diff
-const ControlledInput = ({ value, onValueChange, ...rest }) => {
+const ControlledInput = ({ value, onValueChange, ...rest }) => {
+
+  const handleChange = (e) => {
+    if (rest.type === 'number') {
+      onValueChange(parseInt(e.target.value, 10));
+    } else {
+      onValueChange(e.target.value);
+    }
+  };
+
+  return (
+    <input
+      type={rest.type}
+      value={value}
+      onChange={handleChange}
+      {...rest}
```

#### DataTable (task/48)

```diff
-const DataTable = ({ data }) => {
+const DataTable = ({ data }) => {
+
+  return (
+    <div className="table-container">
+      <table className="table table-striped table-bordered">
+        <thead>
+          <tr>
+            <th>Date</th>
+            <th>Description</th>
+            <th>Credit</th>
+            <th>Debit</th>
+            <th>Balance</th>
+          </tr>
+        </thead
```

#### DataTable (task/48)

```diff
-const DataTable = ({ data }) => {
+const DataTable = ({ data }) => {
+
+  return (
+    <table className="table table-hover">
+      <thead>
+        <tr>
+          <th>Name</th>
+          <th>Email</th>
+          <th>Description</th>
+          <th>Status</th>
+          <th>Created At</th>
+          <th>Updated At</th>
+        </tr>
+      </thead>
+      <tbody
```

#### DataTable (task/48)

```diff
-const DataTable = ({ data }) => {
+const DataTable = ({ data }) => {
+
+  const columns = React.useMemo(
+    () => [
+      {
+        Header: 'Name',
+        accessor: 'name',
+      },
+      {
+        Header: 'Info',
+        accessor: 'info',
+      },
+    ],
+    []
+  );
+
+  return (
+    <ReactTable
+      data={data}
+      columns={columns}
+      defaultPageSize={10}
```

#### DataTable (task/48)

```diff
-const DataTable = ({ data }) => {
+const DataTable = ({ data }) => {
+
+  const dataRows = data.map((row, i) => (
+    <tr key={i}>
+      {Object.keys(row).map((key, i) => (
+        <td key={i}>{row[key]}</td>
+      ))}
+    </tr>
+  ));
+
+  return (
+    <Table className="custom-table">
+      <thead>
+        <tr>
```

#### DataTable (task/48)

```diff
-const DataTable = ({ data }) => {
+const DataTable = ({ data }) => {
+
+  return (
+    <TableContainer>
+      <Table aria-label="simple table">
+        <TableHead>
+          <TableRow>
+            <TableCell align="left">Date</TableCell>
+            <TableCell align="left">Description</TableCell>
+            <TableCell align="left">Category</TableCell>
+            <TableCell align="left">Amount</TableCell>
+          </TableRow>
+        </
```

#### useComponentWillUnmount (task/49)

```diff
-const useComponentWillUnmount = onUnmountHandler => {
+const useComponentWillUnmount = onUnmountHandler => {
+
+  const componentWillUnmount = () => {
+    onUnmountHandler()
+  }
+
+  return [componentWillUnmount]
+}
+
+export default useComponentWillUnmount
```

#### useComponentWillUnmount (task/49)

```diff
-const useComponentWillUnmount = onUnmountHandler => {
+const useComponentWillUnmount = onUnmountHandler => {
+
+  useEffect(() => {
+    return () => {
+      onUnmountHandler();
+    };
+  }, []);
+};
+
+const useComponentDidMount = onMountHandler => {
+  useEffect(() => {
+    onMountHandler();
+  }, []);
+};
+
+export { useComponentDidMount, useComponentWillUnmount };
```

#### useComponentWillUnmount (task/49)

```diff
-const useComponentWillUnmount = onUnmountHandler => {
+const useComponentWillUnmount = onUnmountHandler => {
+
+  const componentWillUnmount = props => {
+    if (onUnmountHandler) {
+      onUnmountHandler(props);
+    }
+  };
+
+  return [componentWillUnmount];
+};
+
+export default useComponentWillUnmount;
```

#### useComponentWillUnmount (task/49)

```diff
-const useComponentWillUnmount = onUnmountHandler => {
+const useComponentWillUnmount = onUnmountHandler => {
+
+  const previousComponentWillUnmount =
+    React.Component.prototype.componentWillUnmount;
+
+  React.Component.prototype.componentWillUnmount = function() {
+    if (typeof previousComponentWillUnmount === 'function') {
+      previousComponentWillUnmount.call(this);
+    }
+
+    if (typeof onUnmountHandler === 'function') {
+      onUnmountHandler.call(this);
+    }
```

#### useComponentWillUnmount (task/49)

```diff
-const useComponentWillUnmount = onUnmountHandler => {
+const useComponentWillUnmount = onUnmountHandler => {
+
+  const prevUnmount = useRef();
+  const prevUnmountSet = useRef(false);
+
+  useEffect(() => {
+    prevUnmount.current = onUnmountHandler;
+    prevUnmountSet.current = true;
+  }, [onUnmountHandler]);
+
+  useEffect(() => {
+    if (prevUnmountSet.current) {
+      prevUnmount.current();
+    }
+  }, []
```

#### Tabs (task/50)

```diff
-const TabItem = props => <div {...props} />;
-
-const Tabs = ({ defaultIndex = 0, onTabClick, children }) => {
+const TabItem = props => <div {...props} />;
+
+const Tabs = ({ defaultIndex = 0, onTabClick, children }) => {
+
+  const [activeIndex, setActiveIndex] = useState(defaultIndex);
+
+  const handleTabClick = index => {
+    setActiveIndex(index);
+    onTabClick && onTabClick(index);
+  };
+
+  return (
+    <ul className="tabs">
+      {React.Children.map(children, (child, index) => {
+        const { disabled } = child.props;
+        const
```

#### Tabs (task/50)

```diff
-const TabItem = props => <div {...props} />;
-
-const Tabs = ({ defaultIndex = 0, onTabClick, children }) => {
+const TabItem = props => <div {...props} />;
+
+const Tabs = ({ defaultIndex = 0, onTabClick, children }) => {
+
+  const [currentIndex, setCurrentIndex] = useState(defaultIndex);
+
+  const onClick = index => {
+    setCurrentIndex(index);
+    onTabClick && onTabClick(index);
+  };
+
+  return (
+    <div className="tabs">
+      <ul className="tabs-nav">
+        {React.Children.map(children, (child, index) => {
+          return (
```

#### Tabs (task/50)

```diff
-const TabItem = props => <div {...props} />;
-
-const Tabs = ({ defaultIndex = 0, onTabClick, children }) => {
+const TabItem = props => <div {...props} />;
+
+const Tabs = ({ defaultIndex = 0, onTabClick, children }) => {
+
+  const [currentIndex, setCurrentIndex] = useState(defaultIndex);
+
+  const handleTabClick = index => {
+    setCurrentIndex(index);
+    onTabClick && onTabClick(index);
+  };
+
+  return (
+    <ul className="c-tabs">
+      {React.Children.map(children, (child, index) => {
+        if (!child) {
+          return null;
```

#### Tabs (task/50)

```diff
-const TabItem = props => <div {...props} />;
-
-const Tabs = ({ defaultIndex = 0, onTabClick, children }) => {
+const TabItem = props => <div {...props} />;
+
+const Tabs = ({ defaultIndex = 0, onTabClick, children }) => {
+
+  const [activeIndex, setActiveIndex] = useState(defaultIndex);
+
+  const onClick = (index, disabled) => {
+    if (!disabled) {
+      setActiveIndex(index);
+      onTabClick && onTabClick(index);
+    }
+  };
+
+  return (
+    <div className="tabs">
+      <TabItem onClick={() => onClick(0, children[0].props
```

#### Tabs (task/50)

```diff
-const TabItem = props => <div {...props} />;
-
-const Tabs = ({ defaultIndex = 0, onTabClick, children }) => {
+const TabItem = props => <div {...props} />;
+
+const Tabs = ({ defaultIndex = 0, onTabClick, children }) => {
+
+  const [currentIndex, setCurrentIndex] = useState(defaultIndex);
+
+  const handleTabClick = index => {
+    setCurrentIndex(index);
+    onTabClick && onTabClick(index);
+  };
+
+  return (
+    <div className="tabs">
+      <div className="tabs-nav">
+        {React.Children.map(children, (child, index) => {
+          const
```

#### useNavigatorOnLine (task/51)

```diff
-const getOnLineStatus = () =>
+const getOnLineStatus = () =>
+ {
+  return typeof navigator !== 'undefined' ? navigator.onLine : true;
+};
+
+export default function networkStatus(): Observable<boolean> {
+  return new Observable(subscriber => {
+    const onlineStatus = getOnLineStatus();
+    subscriber.next(onlineStatus);
+
+    const handler = () => {
+      subscriber.next(getOnLineStatus());
+    };
+
+    const eventHandler =
```

#### useNavigatorOnLine (task/51)

```diff
-const getOnLineStatus = () =>
+const getOnLineStatus = () =>
+ {
+  return {
+    type: GET_ONLINE_STATUS,
+    online: online
+  };
+};
+
+export const getOnlineStatus = () => {
+  if (isBrowser) {
+    const status = navigator.onLine;
+    setOnline(status);
+    return status;
+  }
+  return online;
+};
+
+export const setOnline = status => {
+  online = status;
+  if (is
```

#### useNavigatorOnLine (task/51)

```diff
-const getOnLineStatus = () =>
+const getOnLineStatus = () =>
+ {
+  const { app } = window.webviewApis;
+  if (app) {
+    return app.getOnLineStatus();
+  }
+  return false;
+};
+
+const updateOnLineStatus = (status: boolean) => {
+  const { app } = window.webviewApis;
+  if (app) {
+    app.updateOnLineStatus(status);
+  }
+};
+
+// getCurrentUrl
```

#### useNavigatorOnLine (task/51)

```diff
-const getOnLineStatus = () =>
+const getOnLineStatus = () =>
+ {
+  return {
+    type: GET_ONLINE_STATUS,
+    onLineStatus: true
+  };
+};
+
+export const offLineStatus = () => {
+  return {
+    type: OFF_LINE_STATUS,
+    onLineStatus: false
+  };
+};
+
+export const removeUserInfo = () => {
+  return {
+    type: REMOVE_USER_INFO
+  };
+};
+
```

#### useNavigatorOnLine (task/51)

```diff
-const getOnLineStatus = () =>
+const getOnLineStatus = () =>
+ {
+  return (dispatch: Dispatch<ActionTypes>) => {
+    axios.get('https://www.easy-mock.com/mock/5c8a3a14ac2acb3a322b28f5/example/onlineStatus')
+      .then((res) => {
+        if (res.data.code === 0) {
+          dispatch(changeOnLineStatus(res.data.data));
+        }
```

#### PasswordRevealer (task/52)

```diff
-const PasswordRevealer = ({ value }) => {
+const PasswordRevealer = ({ value }) => {
+
+  const [visible, setVisible] = useState(false);
+
+  const handleToggleVisible = () => {
+    setVisible(!visible);
+  };
+
+  return (
+    <>
+      <Input
+        type={visible ? 'text' : 'password'}
+        value={value}
+        endAdornment={
+          <InputAdornment position="end">
+            <IconButton
+              aria
```

#### PasswordRevealer (task/52)

```diff
-const PasswordRevealer = ({ value }) => {
+const PasswordRevealer = ({ value }) => {
+
+  const [showPassword, setShowPassword] = useState(false);
+
+  const toggleShowPassword = () => {
+    setShowPassword(!showPassword);
+  };
+
+  return (
+    <div className="relative">
+      <input
+        type={showPassword ? 'text' : 'password'}
+        value={value}
+        className="w-full px-3 py-2 rounded-md text-sm
```

#### PasswordRevealer (task/52)

```diff
-const PasswordRevealer = ({ value }) => {
+const PasswordRevealer = ({ value }) => {
+
+  const [isRevealed, setIsRevealed] = useState(false);
+
+  return (
+    <div className="py-2 px-4">
+      <RevealPassword
+        value={value}
+        isRevealed={isRevealed}
+        onToggleReveal={() => setIsRevealed(!isRevealed)}
+      />
+    </div>
+  );
```

#### PasswordRevealer (task/52)

```diff
-const PasswordRevealer = ({ value }) => {
+const PasswordRevealer = ({ value }) => {
+
+  const [isRevealed, setIsRevealed] = useState(false);
+
+  return (
+    <div className="password-revealer">
+      <div
+        className="password-revealer__input"
+        onClick={() => setIsRevealed(!isRevealed)}
+      >
+        {value.replace(/./g, '●')}
+      </div>
+      <Tool
```

#### PasswordRevealer (task/52)

```diff
-const PasswordRevealer = ({ value }) => {
+const PasswordRevealer = ({ value }) => {
+
+  const [visible, setVisible] = useState(false);
+
+  return (
+    <React.Fragment>
+      <Input
+        type={visible ? 'text' : 'password'}
+        value={value}
+        onChange={() => {}}
+        endAdornment={
+          <InputAdornment position="end">
+            <IconButton
+              aria-label="toggle password visibility"
+              on
```

#### StarRating (task/53)

```diff
-const Star = ({ marked, starId }) => {
+const Star = ({ marked, starId }) => {
+
+  return (
+    <button
+      className={marked ? "star-active" : "star-inactive"}
+      onClick={() => {
+        starClicked(starId);
+      }}
+    >
+      &#x2605;
+    </button>
+  );
+};
+
+export default Star;
```

#### StarRating (task/53)

```diff
-const Star = ({ marked, starId }) => {
+const Star = ({ marked, starId }) => {
+
+  return (
+    <div className="star" onClick={() => marked(starId)}>
+      <FontAwesomeIcon icon={faStar} />
+    </div>
+  );
+};
+
+export default Star;
```

#### StarRating (task/53)

```diff
-const Star = ({ marked, starId }) => {
+const Star = ({ marked, starId }) => {
+
+  const className = marked ? 'fas fa-star' : 'far fa-star';
+  return <i className={className} id={starId} />;
+};
+
+export default Star;
```

#### StarRating (task/53)

```diff
-const Star = ({ marked, starId }) => {
+const Star = ({ marked, starId }) => {
+
+  const [star, setStar] = useState(starId)
+  const [preview, setPreview] = useState(starId)
+  const [backgroundColor, setBackgroundColor] = useState('#d8e1e8')
+  const [color, setColor] = useState('#000000')
+  const [name, setName] = useState('')
+  const [description, setDescription] = useState
```

#### StarRating (task/53)

```diff
-const Star = ({ marked, starId }) => {
+const Star = ({ marked, starId }) => {
+
+  return (
+    <span
+      onClick={() => handleStarClick(starId)}
+      className={marked ? 'Star__marked' : 'Star'}
+    >
+      *
+    </span>
+  );
+};
+
+export default Star;
```

#### useComponentDidUpdate (task/54)

```diff
-const useComponentDidUpdate = (callback, condition) => {
+const useComponentDidUpdate = (callback, condition) => {
+
+    const userDidUpdate = useCallback(() => {
+        if (!condition || !condition()) return;
+        callback();
+    }, [callback, condition]);
+
+    useEffect(() => {
+        userDidUpdate();
+    }, [userDidUpdate]);
+};
+
+const useComponentWillUpdate = (callback, condition) => {
+    const userWillUpdate = useCallback(() => {
+        if (!condition || !condition()) return;
```

#### useComponentDidUpdate (task/54)

```diff
-const useComponentDidUpdate = (callback, condition) => {
+const useComponentDidUpdate = (callback, condition) => {
+
+  const didUpdate = useCallback(
+    (previousProps, previousState) => {
+      if (condition) {
+        callback(previousProps, previousState);
+      }
+    },
+    [callback, condition]
+  );
+  useEffect(() => {
+    return didUpdate;
+  }, [didUpdate]);
+};
+
+export default useComponentDidUpdate;
```

#### useComponentDidUpdate (task/54)

```diff
-const useComponentDidUpdate = (callback, condition) => {
+const useComponentDidUpdate = (callback, condition) => {
+
+  useEffect(() => {
+    if (condition) {
+      callback();
+    }
+  });
+};
+
+export default useComponentDidUpdate;
```

#### useComponentDidUpdate (task/54)

```diff
-const useComponentDidUpdate = (callback, condition) => {
+const useComponentDidUpdate = (callback, condition) => {
+
+  const prevProps = useRef();
+  const prevState = useRef();
+
+  useEffect(() => {
+    if (condition) {
+      callback();
+    }
+  }, [callback, condition]);
+
+  useEffect(() => {
+    prevProps.current = props;
+    prevState.current = state;
+  });
+};
+
+export default useComponentDidUpdate;
```

#### useComponentDidUpdate (task/54)

```diff
-const useComponentDidUpdate = (callback, condition) => {
+const useComponentDidUpdate = (callback, condition) => {
+
+  const prevProps = useRef();
+  const prevState = useRef();
+
+  const safeCallback = useCallback(callback, [callback]);
+
+  useEffect(() => {
+    if (condition(prevProps.current, prevState.current)) {
+      safeCallback();
+    }
+  }, [condition, safeCallback]);
+
+  useEffect(() => {
+    prevProps.current = props;
+    prevState.
```

#### Toggle (task/55)

```diff
-const Toggle = ({ defaultToggled = false }) => {
+const Toggle = ({ defaultToggled = false }) => {
+
+  const [toggled, setToggled] = useState(defaultToggled);
+
+  const handleClick = () => {
+    setToggled(!toggled);
+  };
+
+  return (
+    <button onClick={handleClick}>
+      {toggled ? "Toggled" : "Untoggled"}
+    </button>
+  );
+};
+
+export default Toggle;
```

#### Toggle (task/55)

```diff
-const Toggle = ({ defaultToggled = false }) => {
+const Toggle = ({ defaultToggled = false }) => {
+
+  const [isToggled, setIsToggled] = useState(defaultToggled);
+
+  const toggle = () => setIsToggled(!isToggled);
+
+  return (
+    <button className="toggle" onClick={toggle}>
+      <span className="toggle__round" />
+      <span className="toggle__label">{isToggled ? 'ON' : 'OFF'}
```

#### Toggle (task/55)

```diff
-const Toggle = ({ defaultToggled = false }) => {
+const Toggle = ({ defaultToggled = false }) => {
+
+  const [toggled, setToggled] = useState(defaultToggled);
+
+  const toggle = () => setToggled(!toggled);
+
+  return (
+    <div>
+      <label htmlFor="toggle">
+        <input
+          id="toggle"
+          type="checkbox"
+          checked={toggled}
+          onChange={toggle}
+        />
+        {toggled ?
```

#### Toggle (task/55)

```diff
-const Toggle = ({ defaultToggled = false }) => {
+const Toggle = ({ defaultToggled = false }) => {
+
+  const [isToggled, setIsToggled] = useState(defaultToggled);
+
+  const handleToggle = () => {
+    setIsToggled(!isToggled);
+  };
+
+  return (
+    <Container isToggled={isToggled}>
+      <SwitchLabel>
+        <SwitchToggle onClick={handleToggle}>
+          <SwitchToggleText isT
```

#### Toggle (task/55)

```diff
-const Toggle = ({ defaultToggled = false }) => {
+const Toggle = ({ defaultToggled = false }) => {
+
+  const [toggled, setToggled] = useState(defaultToggled);
+
+  const toggle = () => setToggled(!toggled);
+
+  return (
+    <ToggleButton onClick={toggle} toggled={toggled}>
+      {toggled ? "Yes" : "No"}
+    </ToggleButton>
+  );
+};
+
+export default Toggle;
```

#### MappedTable (task/56)

```diff
-const MappedTable = ({ data, propertyNames }) => {
+const MappedTable = ({ data, propertyNames }) => {
+
+  const colums = propertyNames.map(propertyName => {
+    const func = (value, row) => {
+      if (value) {
+        const [key, value] = value.split(':');
+        const property = getProperty(row, key);
+        return property ? property[value] : null;
+      }
+      return null;
+    };
+    return {
+      title: propertyName,
+      dataIndex
```

#### MappedTable (task/56)

```diff
-const MappedTable = ({ data, propertyNames }) => {
+const MappedTable = ({ data, propertyNames }) => {
+
+  const mapped = data.map(entry => {
+    const mappedRow = propertyNames.map(prop => entry[prop]);
+    return mappedRow;
+  });
+  return mapped;
+};
+
+MappedTable.propTypes = {
+  data: PropTypes.arrayOf(PropTypes.object).isRequired,
+  propertyNames: PropTypes.arrayOf(PropTypes.string).isRequired,
+};
+
+export default M
```

#### MappedTable (task/56)

```diff
-const MappedTable = ({ data, propertyNames }) => {
+const MappedTable = ({ data, propertyNames }) => {
+
+  const mappedData = _.map(data, ({ id, ...row }) => ({
+    id,
+    ..._.mapValues(row, value => (_.isArray(value) ? value.join(', ') : value))
+  }));
+
+  return (
+    <Table
+      headers={propertyNames}
+      data={mappedData}
+      className="table-sm"
+      onRowClick={() => null}
```

#### MappedTable (task/56)

```diff
-const MappedTable = ({ data, propertyNames }) => {
+const MappedTable = ({ data, propertyNames }) => {
+
+  return (
+    <table className="table table-striped">
+      <thead>
+        <tr>
+          {propertyNames.map(propertyName => {
+            return <th key={propertyName}>{propertyName}</th>;
+          })}
+        </tr>
+      </thead>
+      <tbody>
+        {data.map(value => {
+          return (
+            <tr key
```

#### MappedTable (task/56)

```diff
-const MappedTable = ({ data, propertyNames }) => {
+const MappedTable = ({ data, propertyNames }) => {
+
+  return (
+    <>
+      {propertyNames.map((name, index) => (
+        <td key={name}>{data[index]}</td>
+      ))}
+    </>
+  );
+};
+
+export default MappedTable;
```

#### useEventListener (task/57)

```diff
-const useEventListener = (type, handler, el = window) => {
+const useEventListener = (type, handler, el = window) => {
+
+  el.addEventListener(type, handler)
+
+  return () => {
+    el.removeEventListener(type, handler)
+  }
+}
+
+export default useEventListener
```

#### useEventListener (task/57)

```diff
-const useEventListener = (type, handler, el = window) => {
+const useEventListener = (type, handler, el = window) => {
+
+  el.addEventListener(type, handler);
+  return () => el.removeEventListener(type, handler);
+};
+
+export const useLockBodyScroll = () => {
+  const [, toggle] = useLockBodyScrollState();
+  return toggle;
+};
+
+export const useLockBodyScrollState = () => {
+  const [locked, setLocked] = useState(false);
+  const toggle = () => set
```

#### useEventListener (task/57)

```diff
-const useEventListener = (type, handler, el = window) => {
+const useEventListener = (type, handler, el = window) => {
+
+    el.addEventListener(type, handler);
+    return () => el.removeEventListener(type, handler);
+};
+
+const useEventCallback = (type, callback) => {
+    const handler = useCallback(event => callback(event), []);
+    useEventListener(type, handler);
+};
+
+export { useEventListener, useEventCallback };
```

#### useEventListener (task/57)

```diff
-const useEventListener = (type, handler, el = window) => {
+const useEventListener = (type, handler, el = window) => {
+
+    el.addEventListener(type, handler);
+    return () => el.removeEventListener(type, handler);
+};
+
+const useWindowSize = () => {
+    const [windowSize, setWindowSize] = useState(() => ({
+        width: window.innerWidth,
+        height: window.innerHeight,
+    }));
+
+    useEffect(() => {
+        const handleResize = () => {
+           
```

#### useEventListener (task/57)

```diff
-const useEventListener = (type, handler, el = window) => {
+const useEventListener = (type, handler, el = window) => {
+
+  el.addEventListener(type, handler);
+  return () => el.removeEventListener(type, handler);
+};
+
+function App() {
+  const [userList, setUserList] = useState([]);
+  const [userName, setUserName] = useState("");
+  const [msgList, setMsgList] = useState([]);
+  const [user, setUser] = useState({});
```

#### Callto (task/58)

```diff
-const Callto = ({ phone, children }) => {
+const Callto = ({ phone, children }) => {
+
+  return (
+    <a href={`tel:${phone}`}>
+      <div className="callto">
+        <span className="callto__icon">
+          <Icon name="phone" />
+        </span>
+        <span className="callto__text">{children}</span>
+      </div>
+    </a>
+  );
+};
+
+export default Callto;
```

#### Callto (task/58)

```diff
-const Callto = ({ phone, children }) => {
+const Callto = ({ phone, children }) => {
+
+  return (
+    <CalltoButton href={`tel:${phone}`} target="_blank">
+      {children}
+    </CalltoButton>
+  );
+};
+
+export default Callto;
```

#### Callto (task/58)

```diff
-const Callto = ({ phone, children }) => {
+const Callto = ({ phone, children }) => {
+
+  return (
+    <a href={`tel:${phone}`} className="text-yellow-500 hover:text-yellow-800">
+      {children}
+    </a>
+  );
+};
+
+export default Callto;
```

#### Callto (task/58)

```diff
-const Callto = ({ phone, children }) => {
+const Callto = ({ phone, children }) => {
+
+  return (
+    <>
+      <a
+        className="callto"
+        href={`tel:${phone}`}
+        target="_blank"
+        rel="noopener noreferrer"
+      >
+        {children}
+      </a>
+    </>
+  );
+};
+
+export default Callto;
```

#### Callto (task/58)

```diff
-const Callto = ({ phone, children }) => {
+const Callto = ({ phone, children }) => {
+
+  return (
+    <div className="callto">
+      <a href={`tel:${phone}`}>{children}</a>
+    </div>
+  );
+};
+
+export default Callto;
```

#### useOnWindowResize (task/59)

```diff
-const useOnWindowResize = callback => {
+const useOnWindowResize = callback => {
+
+	const throttledCallback = useCallback(
+		throttle(callback, 200),
+		[callback]
+	);
+
+	useEffect(() => {
+		window.addEventListener('resize', throttledCallback);
+
+		return () => {
+			window.removeEventListener('resize', throttledCallback);
+		};
+	}, [throttledCallback]);
+};
+
+const Feed = () =>
```

#### useOnWindowResize (task/59)

```diff
-const useOnWindowResize = callback => {
+const useOnWindowResize = callback => {
+
+	const onResize = useCallback(() => {
+		callback(window.innerWidth);
+	}, [callback]);
+
+	useEffect(() => {
+		window.addEventListener('resize', onResize);
+		return () => {
+			window.removeEventListener('resize', onResize);
+		};
+	}, [onResize]);
+};
+
+export default useOnWindowRes
```

#### useOnWindowResize (task/59)

```diff
-const useOnWindowResize = callback => {
+const useOnWindowResize = callback => {
+
+  useEffect(() => {
+    const listener = () => {
+      callback();
+    };
+    window.addEventListener('resize', listener);
+    return () => {
+      window.removeEventListener('resize', listener);
+    };
+  }, [callback]);
+};
+
+const WindowListener = ({ callback }) => {
+  useOnWindowResize(callback);
+  return null;
+};
+
+export default Window
```

#### useOnWindowResize (task/59)

```diff
-const useOnWindowResize = callback => {
+const useOnWindowResize = callback => {
+
+  const handleResize = () => {
+    callback();
+  };
+
+  useEffect(() => {
+    window.addEventListener('resize', handleResize);
+    return () => {
+      window.removeEventListener('resize', handleResize);
+    };
+  }, []);
+};
+
+export default useOnWindowResize;
```

#### useOnWindowResize (task/59)

```diff
-const useOnWindowResize = callback => {
+const useOnWindowResize = callback => {
+
+  const handleResize = () => {
+    callback();
+  };
+
+  useEffect(() => {
+    window.addEventListener('resize', handleResize);
+    return () => {
+      window.removeEventListener('resize', handleResize);
+    };
+  }, []);
+};
+
+const useIsMobile = useCallback(() => {
+  const isMobile = useMediaQuery(MOBILE_BRE
```

#### UncontrolledInput (task/60)

```diff
-const UncontrolledInput = ({ defaultValue, onValueChange, ...rest }) => {
+const UncontrolledInput = ({ defaultValue, onValueChange, ...rest }) => {
+
+  const [value, setValue] = useState(defaultValue);
+
+  useEffect(() => {
+    setValue(defaultValue);
+  }, [defaultValue]);
+
+  const handleValueChange = useCallback(event => {
+    setValue(event.target.value);
+    onValueChange(event.target.value);
+  }, [onValueChange]);
+
+  return (
+    <Input
+      type="text"
+     
```

#### UncontrolledInput (task/60)

```diff
-const UncontrolledInput = ({ defaultValue, onValueChange, ...rest }) => {
+const UncontrolledInput = ({ defaultValue, onValueChange, ...rest }) => {
+
+  const [value, setValue] = useState(defaultValue);
+
+  useEffect(() => {
+    setValue(defaultValue);
+  }, [defaultValue]);
+
+  const onChange = useCallback(
+    e => {
+      setValue(e.target.value);
+      onValueChange(e.target.value);
+    },
+    [onValueChange]
+  );
+
+  return <input onChange={onChange
```

#### UncontrolledInput (task/60)

```diff
-const UncontrolledInput = ({ defaultValue, onValueChange, ...rest }) => {
+const UncontrolledInput = ({ defaultValue, onValueChange, ...rest }) => {
+
+  const onChange = useEventCallback(event => onValueChange(event.target.value));
+
+  return <input defaultValue={defaultValue} onChange={onChange} {...rest} />;
+};
+
+export default UncontrolledInput;
```

#### UncontrolledInput (task/60)

```diff
-const UncontrolledInput = ({ defaultValue, onValueChange, ...rest }) => {
+const UncontrolledInput = ({ defaultValue, onValueChange, ...rest }) => {
+
+  const [value, setValue] = useState(defaultValue);
+
+  const onChange = useCallback(
+    e => {
+      const nextValue = e.target.value;
+      setValue(nextValue);
+      onValueChange(nextValue);
+    },
+    [onValueChange]
+  );
+
+  return <input onChange={onChange} {...rest} value={value} />;
+};
+
+export default
```

#### UncontrolledInput (task/60)

```diff
-const UncontrolledInput = ({ defaultValue, onValueChange, ...rest }) => {
+const UncontrolledInput = ({ defaultValue, onValueChange, ...rest }) => {
+
+  const [value, setValue] = useState(defaultValue);
+
+  useEffect(() => {
+    setValue(defaultValue);
+  }, [defaultValue]);
+
+  const handleValueChange = useCallback(
+    e => {
+      setValue(e.target.value);
+      onValueChange(e.target.value);
+    },
+    [onValueChange]
+  );
+
+  return (
+    <input {
```

#### TextArea (task/61)

```diff
-const TextArea = ({
+const TextArea = ({
+ name, label, error, ...rest }) => {
+  return (
+    <div className="form-group">
+      <label htmlFor={name}>{label}</label>
+      <textarea {...rest} name={name} id={name} className="form-control" />
+      {error && <div className="alert alert-danger">{error}</div>}
+    </div>
+  );
+};
```

#### TextArea (task/61)

```diff
-const TextArea = ({
+const TextArea = ({
+ label, name, value, error, onChange, onBlur, disabled, maxLength }) => {
+  return (
+    <div className="form-group">
+      <label htmlFor={name}>{label}</label>
+      <textarea
+        className="form-control"
+        id={name}
+        name={name}
+        value={value}
+        onChange={onChange}
+        onBlur={on
```

#### TextArea (task/61)

```diff
-const TextArea = ({
+const TextArea = ({
+
+  name,
+  placeholder,
+  value,
+  isMulti,
+  ...rest
+}: TextAreaProps) => {
+  return (
+    <StyledTextArea name={name} placeholder={placeholder} value={value} {...rest} />
+  );
+};
+
+export default TextArea;
```

#### TextArea (task/61)

```diff
-const TextArea = ({
+const TextArea = ({
+
+  name,
+  label,
+  error,
+  ...rest
+}) => {
+  return (
+    <div className="form-group">
+      <label htmlFor={name}>{label}</label>
+      <textarea
+        className="form-control"
+        id={name}
+        name={name}
+        {...rest}
+      />
+      {error && <div className="alert alert-danger
```

#### TextArea (task/61)

```diff
-const TextArea = ({
+const TextArea = ({
+ name, rows, label, error, ...rest }) => {
+  return (
+    <div className="form-group">
+      <label htmlFor={name}>{label}</label>
+      <textarea
+        className="form-control"
+        rows={rows}
+        name={name}
+        id={name}
+        {...rest}
+      />
+      {error && <div className="alert alert-danger">
```

#### useScript (task/62)

```diff
-const useScript = src => {
+const useScript = src => {
+
+    const [state, setState] = useState({
+        loaded: false,
+        error: false
+    });
+
+    useEffect(() => {
+        const script = document.createElement("script");
+        script.src = src;
+        script.async = true;
+
+        script.onload = () => {
+            setState({
+                loaded: true,
+                error: false
+            });
+        };
+
+        script
```

#### useScript (task/62)

```diff
-const useScript = src => {
+const useScript = src => {
+
+    const [state, setState] = useState({
+        loaded: false,
+        error: false
+    });
+
+    useEffect(() => {
+        const script = document.createElement('script');
+        script.src = src;
+        script.async = true;
+
+        script.onload = () => {
+            setState({
+                loaded: true,
+                error: false
+            });
+        };
+
+        script
```

#### useScript (task/62)

```diff
-const useScript = src => {
+const useScript = src => {
+
+  let script = document.createElement('script');
+  script.src = src;
+  script.async = true;
+  document.body.appendChild(script);
+};
+
+// IFrame
+const IFrame = ({ src, height, width, ...rest }) => {
+  const props = { ...rest };
+  const iframe = useRef(null);
+  const scriptSrc =
+    src.indexOf('http
```

#### useScript (task/62)

```diff
-const useScript = src => {
+const useScript = src => {
+
+    useEffect(() => {
+        const script = document.createElement('script');
+        script.src = src;
+        document.body.appendChild(script);
+        return () => {
+            document.body.removeChild(script);
+        };
+    }, [src]);
+};
+
+export default function Sankey({ height, width, data }) {
+    useScript('https://unpkg.com/@antv/data
```

#### useScript (task/62)

```diff
-const useScript = src => {
+const useScript = src => {
+
+  const ref = useRef()
+  useEffect(() => {
+    if (!ref.current) {
+      const script = document.createElement('script')
+      script.src = src
+      ref.current = script
+      document.body.appendChild(script)
+    }
+  }, [src]) // Only re-run if value changes
+  return ref
+}
+
+const useStyles = makeStyles({
+  img
```

#### useRequestAnimationFrame (task/63)

```diff
-const useRequestAnimationFrame = callback => {
+const useRequestAnimationFrame = callback => {
+
+  const requestAnimationFrame =
+    window.requestAnimationFrame ||
+    window.mozRequestAnimationFrame ||
+    window.webkitRequestAnimationFrame ||
+    window.msRequestAnimationFrame;
+  const frameDeadline = window.performance.now() + FRAME_THRESHOLD;
+  requestAnimationFrame(callback);
+  return () => {
+    requestAnimationFrame(() => {
+      if (window.performance.now() >=
```

#### useRequestAnimationFrame (task/63)

```diff
-const useRequestAnimationFrame = callback => {
+const useRequestAnimationFrame = callback => {
+
+    const requestAnimationFrame =
+        window.requestAnimationFrame ||
+        window.mozRequestAnimationFrame ||
+        window.webkitRequestAnimationFrame ||
+        window.msRequestAnimationFrame;
+    const raf = requestAnimationFrame(callback);
+    return () => {
+        requestAnimationFrame.cancel(raf);
+    };
+};
+
+const useMouseCoords = initialX => {
+    const [mouseX, setMouseX
```

#### useRequestAnimationFrame (task/63)

```diff
-const useRequestAnimationFrame = callback => {
+const useRequestAnimationFrame = callback => {
+
+  const element = useRef();
+  useEffect(() => {
+    element.current = requestAnimationFrame(callback);
+    return () => cancelAnimationFrame(element.current);
+  }, [callback]);
+};
+
+export default useRequestAnimationFrame;
```

#### useRequestAnimationFrame (task/63)

```diff
-const useRequestAnimationFrame = callback => {
+const useRequestAnimationFrame = callback => {
+
+  const savedCallback = useRef();
+
+  // Remember the latest callback.
+  useEffect(() => {
+    savedCallback.current = callback;
+  }, [callback]);
+
+  // Set up the interval.
+  useEffect(() => {
+    function tick() {
+      savedCallback.current();
+    }
+    if (savedCallback.current) {
+      const id = setInterval(tick, 1000 / 60);
```

#### useRequestAnimationFrame (task/63)

```diff
-const useRequestAnimationFrame = callback => {
+const useRequestAnimationFrame = callback => {
+
+  const frame = requestAnimationFrame(() => {
+    if (frame !== null) {
+      cancelAnimationFrame(frame);
+    }
+    callback();
+  });
+};
+
+const useInterval = (callback, delay) => {
+  const interval = setInterval(callback, delay);
+  useEffect(() => {
+    return () => {
+      clearInterval(interval);
+    };
+  }, [
```

#### useSet (task/64)

```diff
-const useSet = initialValue => {
+const useSet = initialValue => {
+
+    const [value, setValue] = useState(initialValue);
+    return [value, setValue];
+};
+
+export default useSet;
```

#### useSet (task/64)

```diff
-const useSet = initialValue => {
+const useSet = initialValue => {
+
+  const [state, setState] = useState(initialValue);
+  return [state, setState];
+};
+
+export default useSet;
```

#### useSet (task/64)

```diff
-const useSet = initialValue => {
+const useSet = initialValue => {
+
+  const [state, setState] = useState(initialValue);
+  return [state, setState];
+};
+
+const useSubscribe = (callback, deps) => {
+  const [, forceUpdate] = useState();
+  useEffect(() => {
+    callback();
+    return () => {
+      callback = () => {};
+    };
+  }, deps || []);
+  return forceUpdate;
+};
```

#### useSet (task/64)

```diff
-const useSet = initialValue => {
+const useSet = initialValue => {
+
+  const [value, setValue] = useState(initialValue);
+  return [value, setValue];
+};
+
+export default useSet;
```

#### useSet (task/64)

```diff
-const useSet = initialValue => {
+const useSet = initialValue => {
+
+  const [value, setValue] = useState(initialValue);
+  return [value, setValue];
+};
+
+export default useSet;
```

#### useLocalStorage (task/65)

```diff
-const useLocalStorage = (keyName, defaultValue) => {
+const useLocalStorage = (keyName, defaultValue) => {
+
+  const [state, setState] = useState(() => {
+    try {
+      const val = localStorage.getItem(keyName);
+      return val ? JSON.parse(val) : defaultValue;
+    } catch (e) {
+      return defaultValue;
+    }
+  });
+
+  const set = useCallback(
+    val => {
+      try {
+        const valString = JSON.stringify(val);
```

#### useLocalStorage (task/65)

```diff
-const useLocalStorage = (keyName, defaultValue) => {
+const useLocalStorage = (keyName, defaultValue) => {
+
+  const [storedValue, setStoredValue] = useState(() => {
+    try {
+      const item = window.localStorage.getItem(keyName);
+      return item ? JSON.parse(item) : defaultValue;
+    } catch (error) {
+      console.log(error);
+      return defaultValue;
+    }
+  });
+
+  const setValue = (value) => {
+    try {
```

#### useLocalStorage (task/65)

```diff
-const useLocalStorage = (keyName, defaultValue) => {
+const useLocalStorage = (keyName, defaultValue) => {
+
+  const [localValue, setLocalValue] = useState(
+    getLocalStorageValue(keyName, defaultValue)
+  );
+
+  const setValue = value => {
+    setLocalValue(value);
+    setLocalStorageValue(keyName, value);
+  };
+
+  return [localValue, setValue];
+};
+
+export default useLocalStorage;
```

#### useLocalStorage (task/65)

```diff
-const useLocalStorage = (keyName, defaultValue) => {
+const useLocalStorage = (keyName, defaultValue) => {
+
+  const [data, setData] = useState(defaultValue);
+
+  useEffect(() => {
+    const dataFromStorage = JSON.parse(localStorage.getItem(keyName));
+    if (dataFromStorage) {
+      setData(dataFromStorage);
+    }
+  }, [keyName]);
+
+  useEffect(() => {
+    localStorage.setItem(keyName, JSON.stringify(data));
```

#### useLocalStorage (task/65)

```diff
-const useLocalStorage = (keyName, defaultValue) => {
+const useLocalStorage = (keyName, defaultValue) => {
+
+  const [data, setData] = useState(() => {
+    const storageValue = localStorage.getItem(keyName);
+    if (storageValue) {
+      return JSON.parse(storageValue);
+    }
+    return defaultValue;
+  });
+
+  const setLocalStorage = value => {
+    const valueToStore =
+      value instanceof Function ? value(data) : value;
+    localStorage.setItem
```

#### Collapse (task/66)

```diff
-const Collapse = ({ collapsed, children }) => {
+const Collapse = ({ collapsed, children }) => {
+
+  return collapsed ? null : children;
+};
+
+export default Collapse;
```

#### Collapse (task/66)

```diff
-const Collapse = ({ collapsed, children }) => {
+const Collapse = ({ collapsed, children }) => {
+
+  const [width, setWidth] = useState(getWidth(collapsed));
+
+  useEffect(() => {
+    window.addEventListener('resize', () => {
+      setWidth(getWidth(collapsed));
+    });
+  }, [collapsed]);
+
+  return (
+    <>
+      <div
+        style={{
+          overflowY: 'auto',
+          overflowX: 'hidden',
+          width:
```

#### Collapse (task/66)

```diff
-const Collapse = ({ collapsed, children }) => {
+const Collapse = ({ collapsed, children }) => {
+
+  const isMobile = useMediaQuery({ maxWidth: 768 });
+  const containerStyle = {
+    display: 'flex',
+    flexDirection: 'column',
+    justifyContent: 'center',
+    alignItems: 'center',
+    height: isMobile ? '100vh' : 'auto',
+    margin: '0 0 1em 0',
+  };
+  const svgStyle = {
+    width: '75%
```

#### Collapse (task/66)

```diff
-const Collapse = ({ collapsed, children }) => {
+const Collapse = ({ collapsed, children }) => {
+
+  const isOpen = !collapsed;
+  return (
+    <div className={`collapse ${isOpen ? 'is-open' : ''}`}>
+      {children}
+    </div>
+  );
+};
+
+Collapse.propTypes = {
+  collapsed: PropTypes.bool,
+  children: PropTypes.node,
+};
+
+Collapse.defaultProps = {
+  collapsed: false,
```

#### Collapse (task/66)

```diff
-const Collapse = ({ collapsed, children }) => {
+const Collapse = ({ collapsed, children }) => {
+
+  const style = collapsed ? { display: 'none' } : {};
+  return <div style={style}>{children}</div>;
+};
+
+Collapse.propTypes = {
+  collapsed: PropTypes.bool.isRequired,
+  children: PropTypes.node.isRequired,
+};
+
+export default Collapse;
```

#### RippleButton (task/67)

```diff
-const RippleButton = ({ children, onClick }) => {
+const RippleButton = ({ children, onClick }) => {
+
+  const [ripples, setRipples] = useState([]);
+
+  const startRipple = useCallback(
+    event => {
+      setRipples(prevRipples => [
+        ...prevRipples,
+        <Ripple key={Date.now()} />,
+      ]);
+    },
+    [setRipples],
+  );
+
+  const endRipple = useCallback(
+    event => {
+      set
```

#### RippleButton (task/67)

```diff
-const RippleButton = ({ children, onClick }) => {
+const RippleButton = ({ children, onClick }) => {
+
+  const [ripples, setRipples] = useState([]);
+
+  const clickHandler = (e) => {
+    setRipples([
+      ...ripples,
+      <Ripple key={Math.random()} />,
+    ]);
+    onClick(e);
+  };
+
+  return (
+    <button onClick={clickHandler}>
+      {children}
+      {ripples}
+    </button>
```

#### RippleButton (task/67)

```diff
-const RippleButton = ({ children, onClick }) => {
+const RippleButton = ({ children, onClick }) => {
+
+  const handleClick = (e) => {
+    e.preventDefault();
+    onClick();
+  };
+
+  return (
+    <button
+      onClick={handleClick}
+      className="border border-gray-400 hover:bg-gray-400 bg-transparent hover:text-gray-700 font-semibold hover:border-transparent rounded py-2 px-4"
+    >
+      {
```

#### RippleButton (task/67)

```diff
-const RippleButton = ({ children, onClick }) => {
+const RippleButton = ({ children, onClick }) => {
+
+  const wrapperRef = useRef(null);
+  const [shouldBlur, setShouldBlur] = useState(false);
+
+  const handleMouseDown = (e) => {
+    setShouldBlur(true);
+    e.persist();
+    e.stopPropagation();
+    e.nativeEvent.stopImmediatePropagation();
+  };
+
+  const handleMouseUp = (e) => {
+    set
```

#### RippleButton (task/67)

```diff
-const RippleButton = ({ children, onClick }) => {
+const RippleButton = ({ children, onClick }) => {
+
+  const [ripple, setRipple] = useState([]);
+  const classes = useStyles();
+
+  const handleMouseDown = (event) => {
+    setRipple([
+      {
+        top: event.clientY,
+        left: event.clientX,
+      },
+    ]);
+  };
+
+  const handleMouseUp = () => {
+    setRipple([]);
+  };
+
+  const
```

#### useMutationObserver (task/68)

```diff
-const useMutationObserver = (
+const useMutationObserver = (
+() => {
+  const MutationObserver = (window as any).MutationObserver;
+  const isNative = MutationObserver !== undefined;
+  if (isNative) {
+    return () => {
+      const observer = new MutationObserver(callback);
+      return {
+        observe: observer.observe,
+        disconnect: observer.disconnect,
+      };
+    };
+  }
+  const prefixes
```

#### useMutationObserver (task/68)

```diff
-const useMutationObserver = (
+const useMutationObserver = (
+): {
+  observe: (element: HTMLElement) => void;
+  disconnect: () => void;
+} => {
+  const observer = new MutationObserver(
+    (mutations) => {
+      mutations.forEach((mutation) => {
+        if (mutation.type === 'attributes') {
+          mutation.attributeName === 'data-name' &&
+            mutation.target.dispatchEvent(new Event
```

#### useMutationObserver (task/68)

```diff
-const useMutationObserver = (
+const useMutationObserver = (
+callback: Function) => {
+  let observer: MutationObserver;
+  let fn: Function;
+  const callback2 = (mutations: MutationRecord[], observer: MutationObserver) => {
+    callback(mutations, observer);
+  };
+  const getObserver = () => {
+    if (!observer) {
+      observer = new MutationObserver(callback2);
+    }
+    return observer;
```

#### useMutationObserver (task/68)

```diff
-const useMutationObserver = (
+const useMutationObserver = (
+options) => {
+  const observers = new WeakMap();
+  return {
+    /**
+     * @function useMutationObserver
+     * @description callback will be called if element changes
+     * @param {HTMLElement} el
+     * @param {Function} cb
+     * @param {Object} options
+     * @returns {Object}
+     */
+    on: (el, cb, options) => {
```

#### useMutationObserver (task/68)

```diff
-const useMutationObserver = (
+const useMutationObserver = (
+callback) => {
+    const observer = new MutationObserver(callback);
+    observer.observe(document.body, {
+        childList: true,
+        subtree: true,
+    });
+};
+
+export const useMutationObserverEffect = (callback) => {
+    useEffect(() => {
+        useMutationObserver(callback);
+    }, []);
+};
```

#### Tooltip (task/69)

```diff
-const Tooltip = ({ children, text, ...rest }) => {
+const Tooltip = ({ children, text, ...rest }) => {
+
+  return (
+    <TooltipTrigger
+      mouseEnterDelay={0.1}
+      {...rest}
+    >
+      {children}
+      <TooltipContainer>
+        <TooltipArrow />
+        <TooltipText>{text}</TooltipText>
+      </TooltipContainer>
+    </TooltipTrigger>
+  );
+};
+
+Tooltip.propTypes = {
+  children: PropTypes
```

#### Tooltip (task/69)

```diff
-const Tooltip = ({ children, text, ...rest }) => {
+const Tooltip = ({ children, text, ...rest }) => {
+
+  return (
+    <TooltipWrapper {...rest}>
+      {children}
+      <TooltipText>{text}</TooltipText>
+    </TooltipWrapper>
+  );
+};
+
+export default Tooltip;
```

#### Tooltip (task/69)

```diff
-const Tooltip = ({ children, text, ...rest }) => {
+const Tooltip = ({ children, text, ...rest }) => {
+
+  return (
+    <TooltipWrapper {...rest}>
+      {children}
+      <TooltipText>{text}</TooltipText>
+    </TooltipWrapper>
+  );
+};
+
+Tooltip.propTypes = {
+  children: PropTypes.node.isRequired,
+  text: PropTypes.string.isRequired,
+};
+
+export default Tooltip;
```

#### Tooltip (task/69)

```diff
-const Tooltip = ({ children, text, ...rest }) => {
+const Tooltip = ({ children, text, ...rest }) => {
+
+  return (
+    <TooltipEl {...rest}>
+      {children}
+      <span>{text}</span>
+    </TooltipEl>
+  );
+};
+
+Tooltip.propTypes = {
+  children: PropTypes.node.isRequired,
+  text: PropTypes.string.isRequired,
+};
+
+export default Tooltip;
```

#### Tooltip (task/69)

```diff
-const Tooltip = ({ children, text, ...rest }) => {
+const Tooltip = ({ children, text, ...rest }) => {
+
+  return (
+    <TooltipWrapper
+      className="tooltip"
+      tooltip={text}
+      {...rest}
+    >
+      {children}
+    </TooltipWrapper>
+  );
+};
+
+Tooltip.propTypes = {
+  children: PropTypes.node.isRequired,
+  text: PropTypes.string.isRequired,
+};
+
+export default Tooltip;
```

#### useTimeout (task/70)

```diff
-const useTimeout = (callback, delay) => {
+const useTimeout = (callback, delay) => {
+
+  const savedCallback = useRef();
+
+  // Remember the latest callback.
+  useEffect(() => {
+    savedCallback.current = callback;
+  }, [callback]);
+
+  // Set up the interval.
+  useEffect(() => {
+    function tick() {
+      savedCallback.current();
+    }
+    if (delay !== null) {
+      let id = setInterval(tick, delay);
+      return ()
```

#### useTimeout (task/70)

```diff
-const useTimeout = (callback, delay) => {
+const useTimeout = (callback, delay) => {
+
+  const savedCallback = useRef();
+
+  // Remember the latest callback.
+  useEffect(() => {
+    savedCallback.current = callback;
+  }, [callback]);
+
+  // Set up the interval.
+  useEffect(() => {
+    function tick() {
+      savedCallback.current();
+    }
+    if (delay !== null) {
+      let id = setInterval(tick, delay);
+      return ()
```

#### useTimeout (task/70)

```diff
-const useTimeout = (callback, delay) => {
+const useTimeout = (callback, delay) => {
+
+  const savedCallback = useRef();
+
+  // Remember the latest callback.
+  useEffect(() => {
+    savedCallback.current = callback;
+  }, [callback]);
+
+  // Set up the interval.
+  useEffect(() => {
+    function tick() {
+      savedCallback.current();
+    }
+    if (delay !== null) {
+      let id = setInterval(tick, delay);
+      return ()
```

#### useTimeout (task/70)

```diff
-const useTimeout = (callback, delay) => {
+const useTimeout = (callback, delay) => {
+
+  const savedCallback = useRef();
+
+  // Remember the latest callback.
+  useEffect(() => {
+    savedCallback.current = callback;
+  }, [callback]);
+
+  // Set up the interval.
+  useEffect(() => {
+    function tick() {
+      savedCallback.current();
+    }
+    if (delay !== null) {
+      let id = setInterval(tick, delay);
+      return ()
```

#### useTimeout (task/70)

```diff
-const useTimeout = (callback, delay) => {
+const useTimeout = (callback, delay) => {
+
+  const savedCallback = useRef();
+
+  // Remember the latest callback.
+  useEffect(() => {
+    savedCallback.current = callback;
+  }, [callback]);
+
+  // Set up the interval.
+  useEffect(() => {
+    function tick() {
+      savedCallback.current();
+    }
+    if (delay !== null) {
+      let id = setInterval(tick, delay);
+      return ()
```

#### useError (task/71)

```diff
-const useError = err => {
+const useError = err => {
+
+  return {
+    type: ERROR,
+    payload: err
+  };
+};
+
+export const useErrorActions = () => {
+  const dispatch = useDispatch();
+  return {
+    setError: (err: string) => dispatch(useError(err))
+  };
+};
```

#### useError (task/71)

```diff
-const useError = err => {
+const useError = err => {
+
+  console.log(err);
+  return true;
+};
+
+const getData = async (address, month, year) => {
+  try {
+    const response = await fetch(
+      `https://www.nemlig.com/nemlig/api/v1/rest/mandel?address=${address}&month=${month}&year=${year}`
+    );
+    const result = await response.
```

#### useError (task/71)

```diff
-const useError = err => {
+const useError = err => {
+
+  const [errorMessage, setErrorMessage] = useState(err);
+  const [errorStatus, setErrorStatus] = useState(null);
+
+  useEffect(() => {
+    if (err) {
+      setErrorMessage(err.message);
+      setErrorStatus(err.status);
+    }
+  }, [err]);
+
+  return { errorMessage, errorStatus };
+};
+
+export default useError;
```

#### useError (task/71)

```diff
-const useError = err => {
+const useError = err => {
+
+  const [error, setError] = useState(err);
+  return [error, setError];
+};
+
+export default useError;
```

#### useError (task/71)

```diff
-const useError = err => {
+const useError = err => {
+
+  const [error, setError] = useState<string>(err);
+  return [error, setError];
+};
+
+const useLoading = () => {
+  const [loading, setLoading] = useState<boolean>(false);
+  return [loading, setLoading];
+};
+
+const useLoadingSpinner = (loading: boolean) => {
+  const [showSpinner, setShowSpinner] = useState<bo
```

#### useCopyToClipboard (task/72)

```diff
-const useCopyToClipboard = text => {
+const useCopyToClipboard = text => {
+
+  const [copied, setCopied] = useState(false);
+  const handleClick = () => {
+    setCopied(true);
+    copy(text);
+    setTimeout(() => setCopied(false), 1000);
+  };
+  return [copied, handleClick];
+};
+
+const CopyLink = ({ text }) => {
+  const [copied, handleClick] = useCopyToClipboard(
```

#### useCopyToClipboard (task/72)

```diff
-const useCopyToClipboard = text => {
+const useCopyToClipboard = text => {
+
+  const [hasCopied, setHasCopied] = useState(false);
+
+  const copyToClipboard = useCallback(() => {
+    if (hasCopied) return;
+
+    navigator.clipboard.writeText(text);
+    setHasCopied(true);
+
+    setTimeout(() => {
+      setHasCopied(false);
+    }, 2000);
+  }, [text, hasCopied]);
+
```

#### useCopyToClipboard (task/72)

```diff
-const useCopyToClipboard = text => {
+const useCopyToClipboard = text => {
+
+  const [isLoading, setIsLoading] = useState(false);
+  const [isCopied, setIsCopied] = useState(false);
+
+  const copyToClipboard = () => {
+    setIsLoading(true);
+    setIsCopied(true);
+    setTimeout(() => {
+      setIsCopied(false);
+      setIsLoading(false);
+    }, 1500);
+  };
+
```

#### useCopyToClipboard (task/72)

```diff
-const useCopyToClipboard = text => {
+const useCopyToClipboard = text => {
+
+  const [hasCopied, setHasCopied] = useState(false);
+
+  const copyToClipboard = useCallback(() => {
+    if (hasCopied) return;
+
+    copy(text);
+    setHasCopied(true);
+
+    setTimeout(() => {
+      setHasCopied(false);
+    }, 2000);
+  }, [hasCopied, text]);
+
+  return [copyToClip
```

#### useCopyToClipboard (task/72)

```diff
-const useCopyToClipboard = text => {
+const useCopyToClipboard = text => {
+
+	const [isCopied, setIsCopied] = useState(false);
+
+	const onCopy = () => {
+		setIsCopied(true);
+		setTimeout(() => setIsCopied(false), 2000);
+	};
+
+	return [isCopied, onCopy, text];
+};
+
+export default useCopyToClipboard;
```

#### useMap (task/73)

```diff
-const useMap = initialValue => {
+const useMap = initialValue => {
+
+  const [map, setMap] = useState(initialValue);
+
+  const updateMap = (key, value) => {
+    setMap({
+      ...map,
+      [key]: value,
+    });
+  };
+
+  return [map, updateMap];
+};
+
+export default useMap;
```

#### useMap (task/73)

```diff
-const useMap = initialValue => {
+const useMap = initialValue => {
+
+  const [state, setState] = useState(initialValue);
+  const set = key => value => setState({ ...state, [key]: value });
+  return [state, set];
+};
+
+const Person = ({ name, onChange, onRemove }) => {
+  const [nameState, setName] = useMap(name);
+  const [ageState, setAge] = useMap('');
+  const [gender
```

#### useMap (task/73)

```diff
-const useMap = initialValue => {
+const useMap = initialValue => {
+
+  const [state, setState] = useState(initialValue);
+  const setMap = useCallback(newState => {
+    setState(newState);
+  }, []);
+  return [state, setMap];
+};
+
+export default useMap;
```

#### useMap (task/73)

```diff
-const useMap = initialValue => {
+const useMap = initialValue => {
+
+  const map = new Map(initialValue);
+  const get = index => {
+    return map.get(index);
+  };
+  const set = (index, value) => {
+    map.set(index, value);
+  };
+  const has = index => {
+    return map.has(index);
+  };
+  const remove = index => {
+    map.delete(index);
+  };
+  const keys
```

#### useMap (task/73)

```diff
-const useMap = initialValue => {
+const useMap = initialValue => {
+
+    const [state, setState] = useState(initialValue);
+    const setData = data => {
+        setState(data);
+    };
+    return [state, setData];
+};
+
+export default useMap;
```

#### AutoLink (task/74)

```diff
-const AutoLink = ({ text }) => {
+const AutoLink = ({ text }) => {
+
+  const result = reactLinkify({
+    target: '_blank',
+    className: '',
+    componentDecorator: (decoratedHref, decoratedText, key) => (
+      <span key={key}>
+        <a href={decoratedHref}>{decoratedText}</a>
+      </span>
+    ),
+  })(text);
+
+  return <React.Fragment
```

#### AutoLink (task/74)

```diff
-const AutoLink = ({ text }) => {
+const AutoLink = ({ text }) => {
+
+  return (
+    <>
+      <a href={text} className="underline text-blue-600 hover:text-blue-600 no-underline">
+        {text}
+      </a>
+    </>
+  );
+};
+
+export default AutoLink;
```

#### AutoLink (task/74)

```diff
-const AutoLink = ({ text }) => {
+const AutoLink = ({ text }) => {
+
+  const autoLink = useAutoLink(text);
+  return <Text>{autoLink}</Text>;
+};
+
+export default AutoLink;
```

#### AutoLink (task/74)

```diff
-const AutoLink = ({ text }) => {
+const AutoLink = ({ text }) => {
+
+  const [isClicked, setIsClicked] = useState(false);
+  const [state, setState] = useState({
+    data: [],
+    isLoading: false,
+    isError: false,
+  });
+
+  const checkForUnclicked = () => {
+    if (isClicked) {
+      const array = state.data.filter((item) => item.text === text);
+      if
```

#### AutoLink (task/74)

```diff
-const AutoLink = ({ text }) => {
+const AutoLink = ({ text }) => {
+
+  const link = 'https://github.com/nireo/generator-nextjs';
+  return (
+    <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-sm font-medium leading-5 bg-orange-200 text-orange-800">
+      {text}
+      <span className="ml-1.5">
+        <svg
+         
```

#### useDebounce (task/75)

```diff
-const useDebounce = (value, delay) => {
+const useDebounce = (value, delay) => {
+
+  const [debouncedValue, setDebouncedValue] = useState(value);
+
+  useEffect(() => {
+    const handler = setTimeout(() => {
+      setDebouncedValue(value);
+    }, delay);
+
+    return () => {
+      clearTimeout(handler);
+    };
+  }, [value, delay]);
+
+  return debouncedValue;
+};
+
+export default useDebounce;
```

#### useDebounce (task/75)

```diff
-const useDebounce = (value, delay) => {
+const useDebounce = (value, delay) => {
+
+  const [debouncedValue, setDebouncedValue] = useState(value);
+
+  useEffect(() => {
+    const handler = setTimeout(() => {
+      setDebouncedValue(value);
+    }, delay);
+
+    return () => {
+      clearTimeout(handler);
+    };
+  }, [value, delay]);
+
+  return debouncedValue;
+};
+
+const Search = ({ searchUsers, clearUsers, showClear
```

#### useDebounce (task/75)

```diff
-const useDebounce = (value, delay) => {
+const useDebounce = (value, delay) => {
+
+  const [debouncedValue, setDebouncedValue] = useState(value);
+
+  useEffect(() => {
+    const handler = setTimeout(() => {
+      setDebouncedValue(value);
+    }, delay);
+
+    return () => {
+      clearTimeout(handler);
+    };
+  }, [value, delay]);
+
+  return debouncedValue;
+};
+
+export default useDebounce;
```

#### useDebounce (task/75)

```diff
-const useDebounce = (value, delay) => {
+const useDebounce = (value, delay) => {
+
+    const [debouncedValue, setDebouncedValue] = useState(value);
+
+    useEffect(() => {
+        const handler = setTimeout(() => {
+            setDebouncedValue(value);
+        }, delay);
+
+        return () => {
+            clearTimeout(handler);
+        };
+    }, [value, delay]);
+
+    return debouncedValue;
+};
+
+export default useDebounce;
```

#### useDebounce (task/75)

```diff
-const useDebounce = (value, delay) => {
+const useDebounce = (value, delay) => {
+
+  const [debouncedValue, setDebouncedValue] = useState(value);
+
+  useEffect(() => {
+    const handler = setTimeout(() => {
+      setDebouncedValue(value);
+    }, delay);
+
+    return () => {
+      clearTimeout(handler);
+    };
+  }, [value, delay]);
+
+  return debouncedValue;
+};
+
+export default useDebounce;
```

#### useFetch (task/76)

```diff
-const useFetch = (url, options) => {
+const useFetch = (url, options) => {
+
+  const [response, setResponse] = useState(null);
+  const [error, setError] = useState(null);
+  const [isLoading, setIsLoading] = useState(false);
+
+  useEffect(() => {
+    const fetchData = async () => {
+      setIsLoading(true);
+      try {
+        const res = await fetch(url, options);
+        const json = await res.json();
```

#### useFetch (task/76)

```diff
-const useFetch = (url, options) => {
+const useFetch = (url, options) => {
+
+  const [data, setData] = useState(null);
+  const [loading, setLoading] = useState(true);
+  const [error, setError] = useState(null);
+
+  useEffect(() => {
+    setLoading(true);
+    setError(null);
+
+    fetch(url, options)
+      .then(res => {
+        if (!res.ok) {
+          throw new Error(res
```

#### useFetch (task/76)

```diff
-const useFetch = (url, options) => {
+const useFetch = (url, options) => {
+
+  const [data, setData] = useState(null);
+  const [loading, setLoading] = useState(true);
+  const [error, setError] = useState(null);
+
+  useEffect(() => {
+    const fetchData = async () => {
+      try {
+        const res = await fetch(url, options);
+        const json = await res.json();
+        setData(json);
+        set
```

#### useFetch (task/76)

```diff
-const useFetch = (url, options) => {
+const useFetch = (url, options) => {
+
+  const [data, setData] = useState({})
+  const [loading, setLoading] = useState(true)
+  const [error, setError] = useState(null)
+
+  useEffect(() => {
+    const fetchData = async () => {
+      try {
+        const response = await fetch(url, options)
+        const data = await response.json()
+        setData(data)
+        setLoading
```

#### useFetch (task/76)

```diff
-const useFetch = (url, options) => {
+const useFetch = (url, options) => {
+
+    const [data, setData] = useState(null);
+    const [loading, setLoading] = useState(true);
+    const [error, setError] = useState(null);
+
+    useEffect(() => {
+        setLoading(true);
+        fetch(url, options)
+            .then(res => res.json())
+            .then(json => {
+                setData(json);
+                setLoading(
```

#### useOnGlobalEvent (task/77)

```diff
-const useOnGlobalEvent = (type, callback, options) => {
+const useOnGlobalEvent = (type, callback, options) => {
+
+  useEffect(() => {
+    window.addEventListener(type, callback, options);
+    return () => {
+      window.removeEventListener(type, callback, options);
+    };
+  }, [type, callback, options]);
+};
+
+export default useOnGlobalEvent;
```

#### useOnGlobalEvent (task/77)

```diff
-const useOnGlobalEvent = (type, callback, options) => {
+const useOnGlobalEvent = (type, callback, options) => {
+
+  return eventEmitter.on(type, callback, options);
+};
+
+export const useOnType = (type, options) => {
+  const [emitter] = useGlobalEvent(type);
+  const on = useCallback(() => {
+    emitter.on(type, () => options.callback(type));
+  }, [type, options]);
+  useEffect(() => {
+    on();
+  }, [on
```

#### useOnGlobalEvent (task/77)

```diff
-const useOnGlobalEvent = (type, callback, options) => {
+const useOnGlobalEvent = (type, callback, options) => {
+
+  const handleEvent = (event) => {
+    if (event.type === type) {
+      callback(event);
+    }
+  };
+
+  useEffect(() => {
+    if (options) {
+      window.addEventListener(type, handleEvent, options);
+    } else {
+      window.addEventListener(type, handleEvent);
+    }
+
+    return () => {
+      window.removeEventListener(
```

#### useOnGlobalEvent (task/77)

```diff
-const useOnGlobalEvent = (type, callback, options) => {
+const useOnGlobalEvent = (type, callback, options) => {
+
+  const listener = useCallback(() => {
+    try {
+      callback();
+    } catch (error) {
+      console.error(error);
+    }
+  }, [callback]);
+
+  useEffect(() => {
+    document.addEventListener(type, listener, options);
+    return () => {
+      document.removeEventListener(type, listener, options);
+    };
+  }, [type, listener, options]);
```

#### useOnGlobalEvent (task/77)

```diff
-const useOnGlobalEvent = (type, callback, options) => {
+const useOnGlobalEvent = (type, callback, options) => {
+
+  if (typeof window.addEventListener === 'undefined') {
+    return;
+  }
+
+  const listener = (event) => {
+    if (event.type === type) {
+      callback(event);
+    }
+  };
+
+  window.addEventListener(type, listener, options);
+
+  return () => {
+    window.removeEventListener(type, listener);
+  };
+};
+
+export default use
```

